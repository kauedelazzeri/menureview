from flask import Flask, request
import csv

app = Flask(__name__)
filename = 'items2_10-12-2022 201016.csv'
type = 'Gerado'

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    if request.method == "GET":
        # Read the CSV file
        with open('Cardapio\\'+str(type)+'\\'+str(filename), "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        # Get a random day that has not been voted on
        import random
        week_days = [item["week_day"] for item in data if "vote" not in item]
        if len(week_days) == 0:
            return "All days have been voted on. Thanks for your participation!"
        week_day = random.choice(week_days)
        food_items = [item for item in data if item["week_day"] == week_day]

        # Build the HTML response
        response = """
        <html>
        <head>
            <title>Food Feedback</title>
        </head>
        <body>
            <h1>Food Feedback</h1>
            <form action="/" method="post">
                <h2>Day {}</h2>
                """.format(week_day)

        for item in food_items:
            response += """
                <p>{}</p>
                <label for="{}_good">Good</label>
                <input type="radio" id="{}_good" name="{}" value="good">
                <label for="{}_bad">Bad</label>
                <input type="radio" id="{}_bad" name="{}" value="bad">
                <br>
                """.format(item["title"], item["title"], item["title"], item["title"], item["title"], item["title"], item["title"])

        response += """
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
        """
        return response

    if request.method == "POST":
        # Read the CSV file
        with open('Cardapio\\Votado\\'+str(filename), "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        # Update the vote in the CSV file
        week_day = None
        for item in data:
            if request.form.get(item["title"]):
                week_day = item["week_day"]
                item["vote"] = request.form[item["title"]]
                break

        if week_day is None:
            return "No vote was received. Please try again."

        with open('Cardapio\\Votado\\'+str(filename), "w") as file:
            writer = csv.DictWriter(file, fieldnames=["week_day", "title", "k_calories", "category", "vote"])
            writer.writeheader()
            writer.writerows(data)

        return "Thanks for your vote for day {}!".format(week_day)

if __name__ == "__main__":
    app.run(debug=True)
