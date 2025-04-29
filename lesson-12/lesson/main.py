import sqlite3
import pyodbc

connect_db = sqlite3.connect('AdventureWorks2019.db')
connection = pyodbc.connect(
                               'DRIVER={SQL Server};'
                               'Server=MSI;'
                               'Database=AdventureWorks2019;'
                               'trusted_Connection=yes;'
                               )
cursor = connection.cursor()

cursor.execute('SELECT * FROM Person.Address')
rows = cursor.fetchall()

columns = [column[0] for column in cursor.description]

data = []
for row in rows:
    row_dict = dict(zip(columns, row))
    data.append(row_dict)

# Print the result
for item in data:
    print(item)


cursor.close()
connection.close()




