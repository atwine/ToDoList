import sqlite3

connection = sqlite3.connect('to_do_list.db',check_same_thread = False)
cursor = connection.cursor()

#table handling the authentication in the app.
cursor.execute(

    """CREATE TABLE clients(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(32)
        );"""

)
#table for items on the to do list
cursor.execute(

    """CREATE TABLE todolist(
        itemname VARCHAR(16),
        itemdescription VARCHAR(40)
        );"""

)
#table for finished items
cursor.execute(

    """CREATE TABLE finisheditems(
        fin_itemname VARCHAR(16),
        fin_itemdescription VARCHAR(40)
        );"""

)


connection.commit()
cursor.close()
connection.close()

# sqlite> select * from users;
# 1|Gordon|Ramsy|Red
# 2|Ironman|Tonny|Gold
