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

    # Three distinct user taste profiles.
    # Categorical values must match a genre/mood present in songs.csv.
    # Numeric values are in the 0.0–1.0 range.
    profiles = {
        "High-Energy Pop": {
            "favorite_genre":      "pop",
            "favorite_mood":       "happy",
            "target_energy":       0.90,    # wants very energetic tracks
            "target_valence":      0.85,    # bright, euphoric feel
            "target_danceability": 0.88,    # highly danceable
            "likes_acoustic":      False,   # prefers polished, produced sound
        },
        "Chill Lofi": {
            "favorite_genre":      "lofi",
            "favorite_mood":       "chill",
            "target_energy":       0.38,    # low-key, relaxed energy
            "target_valence":      0.60,    # calm but not sad
            "target_danceability": 0.58,    # gentle groove, not club-ready
            "likes_acoustic":      True,    # warm, acoustic textures
        },
        "Deep Intense Rock": {
            "favorite_genre":      "rock",
            "favorite_mood":       "intense",
            "target_energy":       0.92,    # raw, driving energy
            "target_valence":      0.35,    # darker, more serious tone
            "target_danceability": 0.55,    # rhythmic but not dance-pop
            "likes_acoustic":      False,   # electric, heavily produced
        },
        # --- Edge / adversarial profiles ---
        "Sad Raver": {
            # No electronic+melancholic song exists; numeric proximity decides winner
            "favorite_genre":      "electronic",
            "favorite_mood":       "melancholic",
            "target_energy":       0.95,
            "target_valence":      0.10,    # wants dark/sad music...
            "target_danceability": 0.95,    # ...but also highly danceable
            "likes_acoustic":      False,
        },
        "Classical Rage": {
            # Both categoricals miss every song; arbitrary numeric winner surfaces
            "favorite_genre":      "classical",
            "favorite_mood":       "angry",
            "target_energy":       0.95,
            "target_valence":      0.10,
            "target_danceability": 0.50,
            "likes_acoustic":      True,
        },
        "Loud Acoustic Fan": {
            # likes_acoustic=True pulls toward low-energy tracks; target_energy pulls opposite
            "favorite_genre":      "folk",
            "favorite_mood":       "dreamy",
            "target_energy":       0.95,
            "target_valence":      0.70,
            "target_danceability": 0.80,
            "likes_acoustic":      True,
        },
        "The Minimalist": {
            # All-zero numeric targets; penalty curve is soft so score margins will be narrow
            "favorite_genre":      "ambient",
            "favorite_mood":       "chill",
            "target_energy":       0.0,
            "target_valence":      0.0,
            "target_danceability": 0.0,
            "likes_acoustic":      False,
        },
        "Dancefloor Obsessed": {
            # target_danceability=1.0 is silently ignored by score_song (never read)
            "favorite_genre":      "hip-hop",
            "favorite_mood":       "energetic",
            "target_energy":       0.50,
            "target_valence":      0.50,
            "target_danceability": 1.0,
            "likes_acoustic":      False,
        },
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 40)
        print(f"  Profile: {profile_name}")
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
