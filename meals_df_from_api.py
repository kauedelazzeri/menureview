# Import necessary modules
import requests
import json
import datetime

INIT_MONTH = 12
END_MONTH = 12
YEAR = 2022
EDGE_ACCESS_COOKIE = "<COOKIE_ACCESS_INTRANET>"
LOCAL = "Jaraguá do Sul"

all_meals = []

#function to return all ISO Timestamp from mondays from a year
def get_all_monday(year):
    first_day = datetime.date(year, INIT_MONTH, 1)
    last_day = datetime.date(year, END_MONTH, 31)
    first_monday = first_day + datetime.timedelta(days=-first_day.weekday(), weeks=1)
    last_monday = last_day + datetime.timedelta(days=-last_day.weekday(), weeks=1)
    current_monday = first_monday
    mondays = []
    while current_monday <= last_monday:
        mondays.append(current_monday.isoformat())
        current_monday += datetime.timedelta(days=7)
    return mondays

mondays = get_all_monday(YEAR)

# Set the API endpoint and headers
endpoint = "https://intranet.weg.net/br//_api/web/lists/getbytitle('Card%C3%A1pios')/items"
headers = {"accept": "application/json;odata=verbose"}
cookies = {"EdgeAccessCookie": EDGE_ACCESS_COOKIE}

# function to group the dataset by specific field
def group_by_field(dataset, field):
    grouped_data = {}
    for data in dataset:
        if data.get(field) not in grouped_data:
            grouped_data[data.get(field)] = []
        grouped_data[data.get(field)].append(data)
        del data[field]
    return grouped_data

# Set the parameters for the API call
def get_meals(date):
    params = {
        "$select": "Kcal, Title, DiaSemana",
        "$filter": "Semana ge datetime'{monday}T00:00:00Z' and Semana le datetime'{monday}T23:59:59Z' and substringof('{local}', Localidade/Title)".format(monday=date, local=LOCAL),
        "$orderby": "TipoItem asc"
    }

    # Make the API call and store the response
    response = requests.get(endpoint, headers=headers, cookies=cookies, params=params)

    # Convert the response to a Python dictionary
    data = json.loads(response.text)

    # Extract the dataset from the response
    dataset = data["d"]["results"]

    meals = []
    for meal in dataset:
        meals.append({
            "Title": meal.get("Title"), 
            "Kcal": meal.get("Kcal"),
            "DiaSemana": meal.get("DiaSemana"),
        })
    
    all_meals.append({
        "date": date,
        "meals": group_by_field(meals, "DiaSemana")
    })

#iterate over all mondays
for monday in mondays:
    get_meals(monday)

print(all_meals)

# SAVE DATASET
with open('meals_dataset.json', 'w') as outfile:
    json.dump(all_meals, outfile)