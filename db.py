
import sqlite3

def init():
    con = sqlite3.connect("movies.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS genres
                (id INTEGER PRIMARY KEY, name TEXT, description TEXT)
                """)
    # cur.execute("""CREATE TABLE IF NOT EXISTS movies
    #             (id INTEGER PRIMARY KEY,
    #             title TEXT,
    #             year INTEGER,
    #             rating REAL,
    #             genre_id INTEGER,
    #             FOREIGN KEY (genre_id) REFERENCES genres(id))
    #             """)