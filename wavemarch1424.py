import sqlite3

connection = sqlite3.connect('wavestr2click.db')

cursor = connection.cursor()


# cursor.execute("CREATE TABLE app(name varchar(12));")

app = cursor.execute("SELECT * FROM app")


                    
    
connection.close()