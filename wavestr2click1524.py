# make your import
import sqlite3

# create a connection e.g test.db
connection = sqlite3.connect("test.db")

# create a cursor, this allows us work with daatabase
cursor = connection.cursor()

# create a table Table - 1
cursor.execute("create table gta (release_year integer, relase_name text, city text)")

# create a table Table - 2
cursor.execute("create table city (gta_city text, real_city text)")


# The raw data
release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto II", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]


# adding multiple data to the data base
cursor.executemany("insert into gta values (?,?,?)", release_list)

cursor.execute("insert into gta values (?,?)", ("Liberty City", ))


# To select from 
cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})

gta_search = cursor.fetchall()
print(gta_search)

print("\n")
# print database 
for row in cursor.execute("select * from gta"):
    print(row)

# close your connection
connection.close