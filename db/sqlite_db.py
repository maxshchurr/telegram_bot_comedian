import sqlite3 as sq


def start_sqlite3():
    global db, cursor
    db = sq.connect('test.db')
    cursor = db.cursor()

    if db:
        print('Connected successfully')

    db.execute('CREATE TABLE IF NOT EXISTS joke_types(type_id INTEGER, joke_type TEXT)')
    db.execute('CREATE TABLE IF NOT EXISTS jokes(joke_id INTEGER, joke TEXT)')

    db.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO joke_types VALUES (?)', tuple(data.values()))
        db.commit()
