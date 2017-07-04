from dbhelper import DBHelper 
from flask import Flask
from flask import render_template
from flask import request
import json
app = Flask(__name__)
DB = DBHelper()

@app.route("/")
def home():
    try:
        crimes = DB.get_all_crimes()
        #print(crimes)
        crimes = json.dumps(crimes)

        #print(crimes)
    except Exception as e:
        print(e)
        crimes = None
    return render_template("home.html", crimes = crimes)

@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    category = request.form.get('category')
    date = request.form.get('date')
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    description = request.form.get('description')
    DB.add_crime(category,date, latitude, longitude, description)
    return home()

@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.form.get("userinput")
        print(data)
        DB.add_input(data)
    except Exception as e:
        print("exception while adding data")
        print(str(e))
    return home()

@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print(e)
    return home()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
