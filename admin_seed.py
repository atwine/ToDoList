import sqlite3

connection = sqlite3.connect('to_do_list.db',check_same_thread = False)

cursor = connection.cursor()

cursor.execute(

    """insert into admins(

    username,
    password

    ) values (
            'Gordon',
            'Ramsy'
    );"""

)

connection.commit()
cursor.close()
connection.close()
