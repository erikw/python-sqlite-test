#!/usr/bin/env python3
import db

def main():
    db_con = db.init()
    movies = db.get_movies(db_con)
    for movie in movies:
        print(f"Title: {movie['title']}, Year: {movie['year']}, Rating: {movie['rating']}, Genre: {movie['genre']}")

    db.close(db_con)



if __name__ == "__main__":
    main()