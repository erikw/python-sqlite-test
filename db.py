import sqlite3
import csv
from movies import Movie

CSV_GENRES = "genres.csv"
CSV_MOVIES = "movies.csv"

SQL_CREATE_GENRES = """CREATE TABLE IF NOT EXISTS genres
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)
                """

SQL_CREATE_MOVIES = """CREATE TABLE IF NOT EXISTS movies
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                year INTEGER,
                rating REAL,
                genre_id INTEGER,
                FOREIGN KEY (genre_id) REFERENCES genres(id))
                """



def insert_genres_from_csv(cur, csv_file):
    with open(csv_file, "r") as file:
        for row in csv.DictReader(file):
            cur.execute("INSERT INTO genres (name, description) VALUES (?, ?)", (row["genre"], row["description"]))
    cur.connection.commit()

def insert_movies_from_csv(cur, csv_file):
    genres = cur.execute("SELECT id, name FROM genres").fetchall()
    genre2id = {genre[1]: genre[0] for genre in genres} 
    with open(csv_file, "r") as file:
        for row in csv.DictReader(file):
            genre_id = genre2id[row["genre"]]
            cur.execute("INSERT INTO movies (title, year, rating, genre_id) VALUES (?, ?, ?, ?)",
                        (row["title"], row["year"], row["rating"], genre_id))
    cur.connection.commit()

def init():
    con = sqlite3.connect("movies.db")
    cur = con.cursor()
    cur.execute(SQL_CREATE_GENRES)
    cur.execute(SQL_CREATE_MOVIES)

    nbr_genres = cur.execute("SELECT COUNT(*) FROM genres").fetchone()[0]
    if nbr_genres == 0:
        insert_genres_from_csv(cur, CSV_GENRES)

    nbr_movies = cur.execute("SELECT COUNT(*) FROM movies").fetchone()[0]
    if nbr_movies == 0:
        insert_movies_from_csv(cur, CSV_MOVIES)

    return con

def close(con):
    con.close()


def get_movies(con):
    cur = con.cursor()
    cur.execute("""
                SELECT m.title, m.year, m.rating, g.name AS genre
                FROM movies AS m
                JOIN genres AS g ON m.genre_id = g.id
                ORDER BY m.year ASC
                """)
    rows = cur.fetchall()
    columns = [column[0] for column in cur.description]
    movies_raw = [dict(zip(columns, row)) for row in rows]
    movies = []
    for movie_raw in movies_raw:
        movies.append(Movie(movie_raw["title"], movie_raw["year"], movie_raw["rating"], movie_raw["genre"]))
    return movies

def insert_movie(db_con, movie):
    cur = db_con.cursor()
    genre_id = cur.execute("SELECT id FROM genres WHERE name = ?", (movie.genre,)).fetchone()[0]
    cur.execute("INSERT INTO movies (title, year, rating, genre_id) VALUES (?, ?, ?, ?)",
                (movie.title, movie.year, movie.rating, genre_id))
    db_con.commit()