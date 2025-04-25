#!/usr/bin/env python3
import db
from movies import Movie

def main():
    db_con = db.init()
    movies = db.get_movies(db_con)
    for movie in movies:
        print(movie)

    movie = Movie("Inception", 2010, 8.8, "action")
    db.insert_movie(db_con, movie)

    db.close(db_con)



if __name__ == "__main__":
    main()