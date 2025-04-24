import sqlite3

SQL_CREATE_GENRES = """CREATE TABLE IF NOT EXISTS genres
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)
                """

SQL_CREATE_MOVIES = """CREATE TABLE IF NOT EXISTS movies
                (id INTEGER PRIMARY KEY,
                title TEXT,
                year INTEGER,
                rating REAL,
                genre_id INTEGER,
                FOREIGN KEY (genre_id) REFERENCES genres(id))
                """

def init():
    con = sqlite3.connect("movies.db")
    cur = con.cursor()
    cur.execute(SQL_CREATE_GENRES)
    cur.execute(SQL_CREATE_MOVIES)