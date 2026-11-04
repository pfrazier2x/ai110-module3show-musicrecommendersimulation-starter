
import csv
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple


# Scoring weights
GENRE_WEIGHT = 2.0
MOOD_WEIGHT = 1.0
ENERGY_WEIGHT = 1.0


@dataclass
class Song:
    """Represents a song and its musical features."""
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
    """Stores a user's music preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool = False


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric values."""
    songs = []

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }

            songs.append(song)

    return songs


def score_song(
    user_prefs: Dict,
    song: Dict
) -> Tuple[float, List[str]]:
    """Calculate a song's score and explain the result."""
    score = 0.0
    reasons = []

    # Genre match
    preferred_genre = str(
        user_prefs.get(
            "genre",
            user_prefs.get("favorite_genre", "")
        )
    ).strip().lower()

    song_genre = str(song["genre"]).strip().lower()

    if preferred_genre and song_genre == preferred_genre:
        score += GENRE_WEIGHT
        reasons.append(
            f"Genre match (+{GENRE_WEIGHT:.2f})"
        )

    # Mood match
    preferred_mood = str(
        user_prefs.get(
            "mood",
            user_prefs.get("favorite_mood", "")
        )
    ).strip().lower()

    song_mood = str(song["mood"]).strip().lower()

    if preferred_mood and song_mood == preferred_mood:
        score += MOOD_WEIGHT
        reasons.append(
            f"Mood match (+{MOOD_WEIGHT:.2f})"
        )

    # Energy similarity
    target_energy = float(
        user_prefs.get(
            "energy",
            user_prefs.get("target_energy", 0.5)
        )
    )

    song_energy = float(song["energy"])

    energy_similarity = max(
        0.0,
        1.0 - abs(song_energy - target_energy)
    )

    energy_points = (
        energy_similarity * ENERGY_WEIGHT
    )

    score += energy_points

    reasons.append(
        f"Energy similarity (+{energy_points:.2f})"
    )

    return round(score, 4), reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top k."""
    if k <= 0:
        return []

    scored_songs = []

    for song in songs:
        score, reasons = score_song(
            user_prefs,
            song
        )

        explanation = ", ".join(reasons)

        scored_songs.append(
            (song, score, explanation)
        )

    # Highest score first
    ranked_songs = sorted(
        scored_songs,
        key=lambda result: result[1],
        reverse=True
    )

    return ranked_songs[:k]


class Recommender:
    """Object-oriented music recommendation system."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(
        self,
        user: UserProfile,
        k: int = 5
    ) -> List[Song]:
        """Return the highest-ranked Song objects."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }

        song_dicts = [
            asdict(song)
            for song in self.songs
        ]

        results = recommend_songs(
            user_prefs,
            song_dicts,
            k
        )

        song_lookup = {
            song.id: song
            for song in self.songs
        }

        return [
            song_lookup[song_data["id"]]
            for song_data, score, explanation in results
        ]

    def explain_recommendation(
        self,
        user: UserProfile,
        song: Song
    ) -> str:
        """Explain why a song matches the user's taste."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }

        score, reasons = score_song(
            user_prefs,
            asdict(song)
        )

        return (
            f"{song.title} by {song.artist} "
            f"received a score of {score:.2f}. "
            f"Reasons: {', '.join(reasons)}."
        )
