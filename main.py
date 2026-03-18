import numpy as np

# Dataset: each row = song features
songs = np.array([
    [0.8, 0.6, 0.7],  # Song 1
    [0.9, 0.7, 0.8],  # Song 2
    [0.2, 0.3, 0.4],  # Song 3
    [0.7, 0.8, 0.6],  # Song 4
    [0.1, 0.2, 0.3]   # Song 5
])

# Cosine similarity function
def cosine_similarity(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)

# Ask user for input
song_number = int(input("Enter song number (1-5): "))

# Select target song
target_song = songs[song_number - 1]

# Store similarities
similarities = []

for i in range(len(songs)):
    sim = cosine_similarity(target_song, songs[i])
    similarities.append((i, sim))

# Sort by similarity (highest first)
similarities.sort(key=lambda x: x[1], reverse=True)

print(f"\nTop 2 recommended songs for Song {song_number}:")

count = 0
for i, sim in similarities:
    if i != (song_number - 1):  # skip same song
        print(f"Song {i+1} with similarity {sim:.2f}")
        count += 1
        if count == 2:
            break