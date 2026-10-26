import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """Recommend Song objects using the shared scoring rules."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs ordered by score."""
        if k <= 0:
            return []

        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }

        def ranking_key(song: Song):
            score, _ = score_song(user_prefs, vars(song))
            return -score, song.id

        return sorted(self.songs, key=ranking_key)[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain the points awarded to a song."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }

        _, reasons = score_song(user_prefs, vars(song))
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV and convert numerical values."""
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])

            for feature in [
                "energy",
                "tempo_bpm",
                "valence",
                "danceability",
                "acousticness",
            ]:
                row[feature] = float(row[feature])

            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate a song's score and explain its points."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 3.0
        reasons.append("Genre match (+3.0)")

    if song["mood"] == user_prefs["mood"]:
        score += 2.0
        reasons.append("Mood match (+2.0)")

    energy_similarity = 1 - abs(
        song["energy"] - user_prefs["energy"]
    )

    score += energy_similarity
    reasons.append(
        f"Energy similarity (+{energy_similarity:.2f})"
    )

    return score, reasons

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Score every song and return the top k recommendations."""
    if k <= 0:
        return []

    results = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        results.append((song, score, explanation))

    ranked = sorted(
        results,
        key=lambda item: (-item[1], item[0]["id"])
    )

    return ranked[:k]

