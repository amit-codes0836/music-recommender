import numpy as np


songs = np.array([
    [0.8, 0.6, 0.7],  
    [0.9, 0.7, 0.8],  
    [0.2, 0.3, 0.4],  
    [0.7, 0.8, 0.6],  
    [0.1, 0.2, 0.3]   
])


def cosine_similarity(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)


song_number = int(input("Enter song number (1-5): "))


target_song = songs[song_number - 1]


similarities = []

for i in range(len(songs)):
    sim = cosine_similarity(target_song, songs[i])
    similarities.append((i, sim))


similarities.sort(key=lambda x: x[1], reverse=True)

print(f"\nTop 2 recommended songs for Song {song_number}:")

count = 0
for i, sim in similarities:
    if i != (song_number - 1):  
        print(f"Song {i+1} with similarity {sim:.2f}")
        count += 1
        if count == 2:
            break
