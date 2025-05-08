
import sqlite3
# 1.

# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Roster (
#         Name TEXT,
#         Species TEXT,
#         Age INTEGER
#     )
# ''')
# conn.commit()
# conn.close()
# print("Database and Roster table created successfully.")


# 2.

# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()
# roster_data = [
#     ('Benjamin Sisko', 'Human', 40),
#     ('Jadzia Dax', 'Trill', 300),
#     ('Kira Nerys', 'Bajoran', 29)
# ]
#
# cursor.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', roster_data)
#
# conn.commit()
# conn.close()
#
# print("Roster table populated successfully.")


# 3.

# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()
# cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ('Ezri Dax', 'Jadzia Dax'))
#
# conn.commit()
# conn.close()
#
# print("Name updated successfully.")


# 4. Display

# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()
# cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
# results = cursor.fetchall()
#
# for name, age in results:
#     print(f"Name: {name}, Age: {age}")
#
# conn.close()