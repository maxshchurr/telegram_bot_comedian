import sqlite3 as sq
import random


def start_sqlite3():
    # global db, cursor
    db = sq.connect("../test.db")
    cursor = db.cursor()

    if db:
        print('Connected successfully')

    db.execute("""
    CREATE TABLE IF NOT EXISTS jokes_shtirlitz(joke_text VARCHAR(600));
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS jokes_programmers(
        joke_text VARCHAR(600));
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS jokes_vovochka(joke_text VARCHAR(600));
        """)

    db.execute("""
           CREATE TABLE IF NOT EXISTS jokes_odesa_humor(joke_text VARCHAR(600));
           """)

    db.execute("""
               CREATE TABLE IF NOT EXISTS jokes_programmers(joke_text VARCHAR(600));
               """)

    db.execute("""
                   CREATE TABLE IF NOT EXISTS jokes_about_clowns(joke_text VARCHAR(600));
                   """)

    db.execute("""
                       CREATE TABLE IF NOT EXISTS jokes_about_georgians(joke_text VARCHAR(600));
                       """)

    db.commit()


start_sqlite3()


async def sql_jokes_about_shtirlitz():
    connect = sq.connect('test.db')
    cursor = connect.cursor()

    query = 'SELECT * FROM jokes_shtirlitz'

    cursor.execute(query)
    data = cursor.fetchall()

    jokes = []
    for i in data:
        jokes.append(i)

    result_arr = []
    for result in jokes:
        result_arr.append(str(result[0]))

    joke_id = random.randint(0, len(result_arr))
    print(result_arr[joke_id], joke_id)
    return result_arr[joke_id]


async def sql_jokes_about_vovochka():
    connect = sq.connect('test.db')
    cursor = connect.cursor()

    query = 'SELECT * FROM jokes_vovochka'

    cursor.execute(query)
    data = cursor.fetchall()

    jokes = []
    for i in data:
        jokes.append(i)

    result_arr = []
    for result in jokes:
        result_arr.append(str(result[0]))

    joke_id = random.randint(0, len(result_arr))
    print(result_arr[joke_id], joke_id)
    return result_arr[joke_id]


async def sql_odesa_humor():
    connect = sq.connect('test.db')
    cursor = connect.cursor()

    query = 'SELECT * FROM jokes_odesa_humor'

    cursor.execute(query)
    data = cursor.fetchall()

    jokes = []
    for i in data:
        jokes.append(i)

    result_arr = []
    for result in jokes:
        result_arr.append(str(result[0]))

    joke_id = random.randint(0, len(result_arr))
    print(result_arr[joke_id], joke_id)
    return result_arr[joke_id]


async def sql_programmers():
    connect = sq.connect('test.db')
    cursor = connect.cursor()

    query = 'SELECT * FROM jokes_programmers'

    cursor.execute(query)
    data = cursor.fetchall()

    jokes = []
    for i in data:
        jokes.append(i)

    result_arr = []
    for result in jokes:
        result_arr.append(str(result[0]))

    joke_id = random.randint(0, len(result_arr))
    print(result_arr[joke_id], joke_id)
    return result_arr[joke_id]


async def sql_jokes_about_clowns():
    connect = sq.connect('test.db')
    cursor = connect.cursor()

    query = 'SELECT * FROM jokes_about_clowns'

    cursor.execute(query)
    data = cursor.fetchall()

    jokes = []
    for i in data:
        jokes.append(i)

    result_arr = []
    for result in jokes:
        result_arr.append(str(result[0]))

    joke_id = random.randint(0, len(result_arr))
    print(result_arr[joke_id], joke_id)
    return result_arr[joke_id]


async def sql_jokes_about_georgians():
    connect = sq.connect('test.db')
    cursor = connect.cursor()

    query = 'SELECT * FROM jokes_about_georgians'

    cursor.execute(query)
    data = cursor.fetchall()

    jokes = []
    for i in data:
        jokes.append(i)

    result_arr = []
    for result in jokes:
        result_arr.append(str(result[0]))

    joke_id = random.randint(0, len(result_arr))
    print(result_arr[joke_id], joke_id)
    return result_arr[joke_id]
