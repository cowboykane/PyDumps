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

genre_counts = {}

# Get genre counts.....

for line in ratings:
    parts = line.split(":")
    genre = parts[0].strip()
    movie = parts[1].strip()
    
    genre_counts[genre] = genre_counts.get(genre, 0) + 1
    
    
print("-- Genre Count --")
for genre, count in genre_counts.items():
    print(f"{genre}: {count}")
    
    
    