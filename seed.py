import sqlite3

connection = sqlite3.connect('to_do_list.db',check_same_thread = False)

cursor = connection.cursor()

cursor.execute(

    """insert into clients(

    username,
    password

    ) values (
            'Gordon',
            'Ramsy'
    );"""

)

cursor.execute(

    """insert into clients(

    username,
    password

    ) values (
            'Ironman',
            'Tonny'
    );"""

)

cursor.execute(

    """insert into clients(

    username,
    password

    ) values (
            'Atwine',
            '12345'
    );"""

)

#insert items into the list of to-do itemdescription

cursor.execute(

    """insert into todolist(

    itemname,
    itemdescription

    ) values (
            'lunch',
            'I need to have lunch with Atwine'
    );"""

)

cursor.execute(

    """insert into todolist(

    itemname,
    itemdescription

    ) values (
            'break',
            'I need to have breakfast with Atwine'
    );"""

)

cursor.execute(

    """insert into todolist(

    itemname,
    itemdescription

    ) values (
            'dinner_lunch',
            'I have to do some amazing stuff with wifey'
    );"""

)

cursor.execute(

    """insert into todolist(

    itemname,
    itemdescription

    ) values (
            'basketball',
            'I have a basketball date with the neighbours boy'
    );"""

)

#insert into finished items TABLE

cursor.execute(

    """insert into finisheditems(

    fin_itemname,
    fin_itemdescription

    ) values (
            'lunch',
            'I need to have lunch with Atwine'
    );"""

)

cursor.execute(

    """insert into finisheditems(

    fin_itemname,
    fin_itemdescription

    ) values (
            'dinner',
            'I need to have dinner with wifey'
    );"""

)

connection.commit()
cursor.close()
connection.close()
