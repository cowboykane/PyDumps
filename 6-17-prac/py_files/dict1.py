ratings = [
    "Crime: The Godfather",
    "Sci-Fi: Blade Runner",
    "Crime: The Godfather",
    "Mystery: Mulholland Drive",
    "Sci-Fi: Blade Runner",
    "Horror: Alien",
    "Crime: The Godfather",
    "Animation: Akira",
    "Mystery: Mulholland Drive",
    "Sci-Fi: Blade Runner",
    "Crime: The Godfather",
    "Animation: Akira",
    "Mystery: Mulholland Drive",
    "Horror: Alien",
    "Sci-Fi: Blade Runner",
    "Crime: The Godfather",
    "Animation: Paprika",
]

movie_count = {}

for item in ratings:
    clean_parts = item.split(":")
    movie_name = clean_parts[1].strip() 
    
    movie_count[movie_name] = movie_count.get(movie_name, 0) + 1


most_rated_movie = max(movie_count, key=movie_count.get)
highest_count = movie_count[most_rated_movie]

print(f"Most Rated Movie: {most_rated_movie} ({highest_count} ratings)\n")

print("--- FULL RATING REPORT ---")
sorted_movies = sorted(movie_count.items(), key=lambda x: x[1], reverse=True)

for movie, count in sorted_movies:
    print(f"{movie}: {count} ratings")
