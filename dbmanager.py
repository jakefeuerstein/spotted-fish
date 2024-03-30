import mysql.connector
import csv
from datetime import datetime

# Connect to DB ----------------------------------------------------------------------

with open('config.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if "pw =" in line:
            pw = str(line[6:-2])

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=pw,
    database="database1"
)

mycursor = mydb.cursor()

# Create database ----------------------------------------------------------------------
# mycursor.execute("CREATE DATABASE database1")
# mycursor.execute("SHOW DATABASES")


# Species table -----

# Create table
# stmt = "CREATE TABLE IF NOT EXISTS species (name VARCHAR(255) PRIMARY KEY)"
# mycursor.execute(stmt)

# Import from CSV
# with open('data/fish_species.csv', mode='r', newline='') as file:
#     # print(file.readlines())
#     csv_file = csv.reader(file)
#     species = []
#     for line in csv_file:
#         species.append(line[0])
    # print("File to arr check: ", species)

# Populate table
# for row in species:
#     mycursor.execute(f'INSERT INTO species (name) VALUES ("{row}")')
# mydb.commit()


# Locations table -----

# Create table
# stmt = "CREATE TABLE IF NOT EXISTS locations (" \
#        "name VARCHAR(255) PRIMARY KEY," \
#        "city VARCHAR(255)," \
#        "state VARCHAR(255)" \
#        ")"
# mycursor.execute(stmt)

# Import from CSV
# with open('data/locations.csv', mode='r') as file:
#     csv_file = csv.reader(file)
#     locations = []
#     for line in csv_file:
#         locations.append(tuple(line))
#     print(locations)

# Populate table
# stmt = "INSERT INTO locations (" \
#        "name," \
#        "city," \
#        "state" \
#        ") VALUES (" \
#        "%s, %s, %s" \
#        ")"
# mycursor.executemany(stmt, locations)
# mydb.commit()


# Logs table -----

# Create table
# mycursor.execute("CREATE TABLE IF NOT EXISTS logs ("
#                  "id INT AUTO_INCREMENT PRIMARY KEY,"
#                  "time DATETIME,"
#                  "location VARCHAR(255) REFERENCES locations(name),"
#                  "activity VARCHAR(255),"
#                  "observed VARCHAR(255),"
#                  "caught VARCHAR(255)"
#                  ")"
#                  )

# Import from CSV
# with open('data/logs.csv', mode='r') as file:
#     csv_file = csv.reader(file)
#     logs = []
#     for i, line in enumerate(csv_file):
#         if i == 0: continue
#         logs.append(line)
#
# for row in logs:
#     dt_str = row[0] + ":00"  # Prep str
#     dt = datetime.strptime(dt_str, '%m/%d/%Y %H:%M:%S') # Convert from str to dt
#     row[0] = dt.strftime('%Y-%m-%d %H:%M:%S')  # Convert to YYYY-MM-DD hh:mm:ss for MySQL
#     row = tuple(row)
#
# # Populate table
# stmt = "INSERT INTO logs (" \
#        "time," \
#        "location," \
#        "activity," \
#        "observed," \
#        "caught" \
#        ") VALUES (%s, %s, %s, %s, %s)"
#
# mycursor.executemany(stmt, logs)
# mydb.commit()


# Actively collect log data


# for x in mycursor:
#     print(x)
#
# sql_formula = "INSERT INTO %s (name, age) VALUES (%s, %s)"
# students = [
#     ("student1", 22)
# ]
#
#
# mycursor.execute(sql_formula, students)
#
# mydb.commit()



# ---------------------------------------------------------------------------

class DBManager:
    def add(self, time: str, location: str, activity: str, observed: str, caught: str):
        stmt = "INSERT INTO logs (" \
               "time," \
               "location, " \
               "activity, " \
               "observed, " \
               "caught" \
               ")" \
               "VALUES (" \
               "%s, %s, %s, %s, %s" \
               ")"
        val = (time, location, activity, observed, caught)
        mycursor.execute(stmt, val)
        mydb.commit()