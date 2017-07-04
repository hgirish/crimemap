import sqlite3
import datetime

class DBHelper:
    def connect(self, database="crimemap"):
        return sqlite3.connect("./db/"+database)

    def get_all_crimes(self):
        connection = self.connect()
        try:
            query = "SELECT latitude, longitude,date, category, description from crimes;"
            cursor = connection.cursor()
            cursor.execute(query)
            named_crimes = []
            for crime in cursor:
                named_crime = {
                    'latitude': crime[0],
                    'longitude': crime[1],
                    'date' : crime[2],
                    'category': crime[3],
                    'description': crime[4]
                }
                named_crimes.append(named_crime)
            
            return named_crimes
        finally:
            cursor.close()
            connection.close()
    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description from crimes;"
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            cursor.close()
            connection.close()
    
    def add_crime(self, category, date, latitude, longitude, description):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (category, date, latitude,longitude, description) VALUES (?,?,?,?,?)"
            cursor = connection.cursor()
            cursor.execute(query, (category,date,latitude,longitude,description))
            connection.commit()
        except Exception as e:
            print(str(e))
        finally:
            cursor.close()
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (description) VALUES (?);"
            
            cursor = connection.cursor()
            cursor.execute(query,(data,))
            connection.commit()

        except Exception as e:
            print(e)
        finally:
            cursor.close()
            connection.close()
    
    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
        finally:
            cursor.close()
            connection.close()
            