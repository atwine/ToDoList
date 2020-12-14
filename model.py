import sqlite3

#fetchall from the database
def fetch():
    connection = sqlite3.connect('to_do_list.db',check_same_thread=False)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute(
    """select * from todolist;"""
    )

    items = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()

    return items



#check the password if its available in the db
def checkpwd(username):
    connection = sqlite3.connect('to_do_list.db',check_same_thread=False)

    cursor = connection.cursor()
    cursor.execute(
    """select password from clients where username = '{username}' order by pk desc;""".format(username = username)
    )

    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return password


#check the password of admin  if its available in the db
def checkpwd_admin(username):
    connection = sqlite3.connect('to_do_list.db',check_same_thread=False)

    cursor = connection.cursor()
    cursor.execute(
    """select password from admins where username = '{username}' order by pk desc;""".format(username = username)
    )

    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return password

#check user
def check_users():
    connection = sqlite3.connect('to_do_list.db',check_same_thread=False)

    cursor = connection.cursor()
    cursor.execute(
    """select  username from clients order by pk desc;"""
    )

    db_users = cursor.fetchall()

    users = []

    #loop through the db db_users
    for i in range (len(db_users)):
        person = db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()

    return users


#this the function that adds people to the database.
def signup(username, password):
    connection = sqlite3.connect('to_do_list.db',check_same_thread=False)

    cursor = connection.cursor()
    #check if the user is there.
    cursor.execute(
    """select password from clients where username = '{username}' order by pk desc;""".format(username = username)
    )
    exist = cursor.fetchone()

    if exist is None:
        cursor.execute(
        """insert into clients (username,password) values('{username}','password');""".format(username=username,password=password)
        )
    else:
        return("User Already Existed!")

    connection.commit()
    cursor.close()
    connection.close()
    #the return of the real function
    return 'You have successfully signed up'

#I need a todo function: which will add a to-do something on the list.
def Todo(itemname, itemdescription):
    connection = sqlite3.connect('to_do_list.db',check_same_thread=False)

    cursor = connection.cursor()
    #check if the user is there.

    cursor.execute(
    """insert into todolist (itemname,itemdescription) values('{itemname}','itemdescription');""".format(itemname=itemname,itemdescription=itemdescription)
    )

    connection.commit()
    cursor.close()
    connection.close()
    #the return of the real function
    return 'You have successfully added an item'
