import sqlite3

connection = sqlite3.connect('to_do_list.db',check_same_thread = False)
cursor = connection.cursor()

#table handling the authentication in the app for admin people.
cursor.execute(

    """CREATE TABLE admins(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(32)
        );"""

)

connection.commit()
cursor.close()
connection.close()

"""
This is the file that controls the admin schema, this means the structure of the database which is going
to hande the admins of the whole application.
"""
