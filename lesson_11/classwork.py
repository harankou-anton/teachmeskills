import sqlite3
from datetime import datetime


def create_table():
    with sqlite3.connect("my_database_11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE user
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname VARCHAR,
            lastname VARCHAR,
            email VARCHAR,
            password VARCHAR,
            age INTEGER,
            datetime DATETIME);
        """)
        session.commit()


# create_table()


def create_user(firstname: str, lastname: str, email: str, password: str, age: int, dt: datetime):
    with sqlite3.connect("my_database_11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute("""
           INSERT INTO user (firstname, lastname, email, password, age, datetime)
           VALUES (?, ?, ?, ?, ?, ?);
           """,
           (firstname, lastname, email, password, age, dt),
                       )
        session.commit()


# create_user('Anton', 'Harankou', 'harankou.anton@gmail.com', 'qwerty', 25, datetime.now())
# create_user('Lionel', 'Messi', 'messi.lionel@gmail.com', 'worldcup', 35, datetime.now())
# create_user('Gareth', 'Bale', 'bale.gareth@gmail.com', 'golf', 33, datetime.now())
# create_user('Cristiano', 'Ronaldo', 'cristiano.ronaldo@gmail.com', 'saudiarabia', 37, datetime.now())
# create_user('Erling', 'Haaland', 'haaland.erling@gmail.com', 'hattrick', 22, datetime.now())


def select_by_name(name: str):
    with sqlite3.connect("my_database_11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute("""
        SELECT * FROM user WHERE firstname = ?;
        """, (name,)
                       )
        session.commit()
        selection = cursor.fetchall()
        print(selection)


# select_by_name('Anton')


def select_by_age(age_1: int, age_2: int):
    with sqlite3.connect("my_database_11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute("""
        SELECT * FROM user WHERE age BETWEEN ? AND ?;
        """, (age_1, age_2)
                       )
        session.commit()
        selection = cursor.fetchall()
        print(selection)


# select_by_age(20, 30)

def select_by_name_or_age():
    name = input('Type a name: ')
    age = int(input('Type an age: '))
    with sqlite3.connect("my_database_11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute("""
        SELECT * FROM user WHERE firstname = ? OR age = ?;
        """, (name, age)
                       )
        session.commit()
        selection = cursor.fetchall()
        print(selection)


select_by_name_or_age()