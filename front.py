from flask import Flask, request
import csv

from jinja2 import Template

template = Template(open('template.html').read())
rendered_template = template.render()
#print(rendered_template)

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

        response += """
                <p>Menu items for the day:</p>
                """
        for item in food_items:
            response += """
                <p>{}</p>
                """.format(item["title"])

        response += """
                <br>
                <label for="vote">Your Vote:</label><br>
                <input type="radio" id="vote_good" name="vote" value="good">
                <label for="vote_good">Good</label><br>
                <input type="radio" id="vote_bad" name="vote" value="bad">
                <label for="vote_bad">Bad</label><br>
                <br>
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

        # Check if the day has already been voted on
        week_day = None
        for item in data:
            if "title" in item:
                vote = request.form.get(item["title"])
                if vote:
                    week_day = item["week_day"]
                    break
        if week_day is None:
            return "No vote was received. Please try again."
        if week_day in [item["week_day"] for item in data if "vote" in item]:
            return "The vote for day {} has already been submitted. Thank you for your participation.".format(week_day)

        # Update the vote in the CSV file
        for item in data:
            if item["week_day"] == week_day:
                item["vote"] = vote

        with open('Cardapio\\Votado\\'+str(filename), "w") as file:
            writer = csv.DictWriter(file, fieldnames=["week_day", "title", "k_calories", "category", "vote"])
            writer.writeheader()
            writer.writerows(data)

        return "Thanks for your vote for day {}!".format(week_day)



if __name__ == "__main__":
    app.run(debug=True)