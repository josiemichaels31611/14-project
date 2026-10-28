movies = [
    ("The Matrix", 1999),
    ("Avatar", 2009),
    ("Jurassic Park", 1993),
    ("Avengers: Endgame", 2019),
    ("Inception", 2010),
    ("Titanic", 1997)
]
movies.sort(key= lambda x : x[-1], reverse= True)
print(movies)