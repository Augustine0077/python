movies = []
ratings = []
while True:
    movie = input("Enter movie name (enter q to quit): ")
    if movie.lower() == "q":
        break
    rating = float(input("Enter rating (1-10): "))
    movies.append(movie)
    ratings.append(rating)
print("Movie Ratings:")
for i in range(len(movies)):
    print(f"{movies[i]}: {ratings[i]}")