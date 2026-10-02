import mysql.connector

# 1. CONNECT
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mlucky@9620",
    database="school"
)

# 2. CURSOR
cursor = connection.cursor()

# 3. INSERT
cursor.execute(
    "INSERT INTO students (name, marks) VALUES (%s, %s)",
    ("Rahul", 85)
)
connection.commit()
print("Inserted")

# 4. SELECT
cursor.execute("SELECT * FROM students")
print("All students:")
for row in cursor.fetchall():
    print(row)

# 5. UPDATE
cursor.execute(
    "UPDATE students SET marks = 90 WHERE name = 'Rahul'"
)
connection.commit()
print("Updated")

# 6. DELETE
cursor.execute(
    "DELETE FROM students WHERE name = 'Rahul'"
)
connection.commit()
print("Deleted")

# 7. CLOSE
cursor.close()
connection.close()
print("Done")
