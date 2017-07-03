import sqlite3

class DBHelper:
    def connect(self, database="crimemap"):
        return sqlite3.connect("./db/"+database)

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
            