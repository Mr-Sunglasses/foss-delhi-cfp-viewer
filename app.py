from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    # Open the CSV file
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        # Convert the CSV data into a list of dictionaries
        data = [row for row in reader]

    # Render the template with the data
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
