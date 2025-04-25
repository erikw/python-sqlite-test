class Movie:
    def __init__(self, title, year, rating, genre):
        self.title = title
        self.year = year
        self.rating = rating
        self.genre = genre

    def __str__(self):
        return f"Movie(title={self.title}, year={self.year}, rating={self.rating}, genre={self.genre})"