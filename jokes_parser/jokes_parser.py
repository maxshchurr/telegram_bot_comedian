from bs4 import BeautifulSoup
import requests
import sqlite3 as sq


class JokesAboutShtirlitz:
    def jokes_about_shtirlitz(self):
        for page in range(1, 22 + 1):

            url = f'https://humornet.ru/anekdot/pro-shtirlica/page/{page}/'
            page = requests.get(url)
            data = page.text
            soup = BeautifulSoup(data, 'html.parser')
            joke_body = soup.find_all('div', class_='text')

            for jokes in joke_body:
                joke = jokes.text
                print(joke)
                db = sq.connect("../test.db")
                cursor = db.cursor()

                cursor.execute("""INSERT INTO jokes_shtirlitz VALUES (?);""", (joke,))
                db.commit()
                db.close()


class JokesAboutVovochka:
    def jokes_about_vovochka(self):
        for page in range(1, 37 + 1):

            url = f'https://humornet.ru/anekdot/vovochka/page/{page}/'
            page = requests.get(url)
            data = page.text
            soup = BeautifulSoup(data, 'html.parser')
            joke_body = soup.find_all('div', class_='text')

            for jokes in joke_body:
                joke = jokes.text
                print(joke)
                db = sq.connect("../test.db")
                cursor = db.cursor()

                cursor.execute("""INSERT INTO jokes_vovochka VALUES (?);""", (joke,))
                db.commit()
                db.close()


class OdesaHumor:
    def get_odesa_humor(self):
        for page in range(1, 20 + 1):

            url = f'https://humornet.ru/anekdot/evrei/page/{page}/'
            page = requests.get(url)
            data = page.text
            soup = BeautifulSoup(data, 'html.parser')
            joke_body = soup.find_all('div', class_='text')

            for jokes in joke_body:
                joke = jokes.text
                print(joke)
                db = sq.connect("../test.db")
                cursor = db.cursor()

                cursor.execute("""INSERT INTO jokes_odesa_humor VALUES (?);""", (joke,))
                db.commit()
                db.close()


class JokesAboutProgrammers:
    def jokes_about_programmers(self):
        for page in range(1, 12 + 1):

            url = f'https://anekdoty.ru/pro-programmistov/page/{page}/'
            page = requests.get(url)
            data = page.text
            soup = BeautifulSoup(data, 'html.parser')
            joke_body = soup.find_all('div', class_='holder-body')

            for jokes in joke_body:
                joke = jokes.text
                print(joke)
                db = sq.connect("../test.db")
                cursor = db.cursor()

                cursor.execute("""INSERT INTO jokes_programmers VALUES (?);""", (joke,))
                db.commit()
                db.close()


class JokesAboutClowns:
    def jokes_about_clowns(self):
        for page in range(1, 2 + 1):

            url = f'https://anekdoty.ru/pro-klounov/page/{page}/'
            page = requests.get(url)
            data = page.text
            soup = BeautifulSoup(data, 'html.parser')
            joke_body = soup.find_all('div', class_='holder-body')

            for jokes in joke_body:
                joke = jokes.text
                print(joke)
                db = sq.connect("../test.db")
                cursor = db.cursor()

                cursor.execute("""INSERT INTO jokes_about_clowns VALUES (?);""", (joke,))
                db.commit()
                db.close()


# UNCOMMENT TO PARSE INTO DB
"""
jokes_shtirlitz = JokesAboutShtirlitz()
jokes_shtirlitz.jokes_about_shtirlitz()

jokes_vovochka = JokesAboutVovochka()
jokes_vovochka.jokes_about_vovochka()

jokes_odesa_humor = OdesaHumor()
jokes_odesa_humor.get_odesa_humor()

jokes_programmers = JokesAboutProgrammers()
jokes_programmers.jokes_about_programmers()
"""

jokes_about_clowns = JokesAboutClowns()
jokes_about_clowns.jokes_about_clowns()

# for page in range(1, 2 + 1):
#
#     url = f'https://anekdoty.ru/pro-klounov/page/{page}/'
#     page = requests.get(url)
#     data = page.text
#     soup = BeautifulSoup(data, 'html.parser')
#     joke_body = soup.find_all('div', class_='holder-body')
#
#     for jokes in joke_body:
#         joke = jokes.text
#         print(joke)
