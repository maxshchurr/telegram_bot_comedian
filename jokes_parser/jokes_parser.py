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


jokes_shtirlitz = JokesAboutShtirlitz()
jokes_shtirlitz.jokes_about_shtirlitz()


class JokesAboutProgrammers:
    def jokes_about_programmers(self):
        pass
#
#
# class OdesaHumor():
#     def get_odesa_humor(self):
#         pass
#
#
# class JokesAboutVovochka:
#     def jokes_about_vovochka(self):
#         pass




# def main():
#     pass
#
#
# if __name__ == '__main__':
#     main()
