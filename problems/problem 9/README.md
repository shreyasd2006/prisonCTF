Description:
Fix the following Python code to prevent SQL injection attacks.

import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn. cursor()

user_input = input("Enter username: ")
query = "SELECT * FROM users WHERE name = '" + user_input + "';"
cursor.execute(query)

print(cursor.fetchall())