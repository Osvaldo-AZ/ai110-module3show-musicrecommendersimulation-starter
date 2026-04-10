"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # User taste profile — values must match feature ranges in songs.csv
    # Categorical: favorite_genre and favorite_mood must match a value in the dataset
    # Numeric:     target_energy, target_valence, target_danceability all 0.0–1.0
    # Boolean:     likes_acoustic — True favors high acousticness, False favors electronic
    user_prefs = {
        "favorite_genre":      "pop",   # matched against song["genre"]
        "favorite_mood":       "happy", # matched against song["mood"]
        "target_energy":       0.80,    # prefers high-energy tracks
        "target_valence":      0.78,    # prefers bright, positive-sounding music
        "target_danceability": 0.80,    # prefers tracks easy to move to
        "likes_acoustic":      False,   # prefers electronic/produced sound
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 40)
    print(f"  Top {len(recommendations)} Recommendations")
    print("=" * 40)
    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Score: {score:.2f}")
        print(f"    Why:")
        for reason in explanation:
            print(f"      - {reason}")
    print("\n" + "-" * 40)


if __name__ == "__main__":
    main()
   # input("\nPress Enter to exit...")
