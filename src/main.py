"""Compare recommendations for different listener profiles."""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.4,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9,
        },
        "Edge Case: High-Energy Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.95,
        },
    }

    for name, user_prefs in profiles.items():
        print(f"\n=== {name} ===")
        print(f"Preferences: {user_prefs}\n")

        recommendations = recommend_songs(
            user_prefs, songs, k=5
        )

        for position, result in enumerate(
            recommendations, start=1
        ):
            song, score, explanation = result
            print(f"{position}. {song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()