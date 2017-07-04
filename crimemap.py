from dbhelper import DBHelper 
from flask import Flask
from flask import render_template
from flask import request
import json
import dateparser
import datetime 
import string

app = Flask(__name__)
DB = DBHelper()

categories = ['mugging', 'break-in']


@app.route("/")
def home(error_message=None):
    try:
        crimes = DB.get_all_crimes()
        #print(crimes)
        crimes = json.dumps(crimes)

        #print(crimes)
    except Exception as e:
        print(e)
        crimes = None
    return render_template("home.html", crimes = crimes,
categories=categories,error_message=error_message)

@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    category = request.form.get('category')
    if category not in categories:
        return home("Invalid category")
    date = format_date(request.form.get('date'))
    if not date:
        return home("Invalid date. Please use yyyy-mm-dd format")
    try:
        latitude = float(request.form.get('latitude'))
        longitude = float(request.form.get('longitude'))
    except ValueError:
        return home("Invalid latitude/longitude")
    description = request.form.get('description')
    description = sanitize_string(description)
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

def format_date(userdate):
    date = dateparser.parse(userdate)
    try:
        return datetime.datetime.strftime(date, "%Y-%m-%d")
    except TypeError:
        return None
def sanitize_string(userinput):
    whitelist = string.ascii_letters + string.digits + " !?$.,;:-'()&"
    return "".join(list(filter(lambda x: x in whitelist, userinput)))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
