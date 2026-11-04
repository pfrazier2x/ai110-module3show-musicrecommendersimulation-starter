
from pathlib import Path
from src import recommender

profiles = {
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.8},
    "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
    "Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9},
}

songs = recommender.load_songs(
    str(Path(__file__).resolve().parents[1] / "data" / "songs.csv")
)

original_weights = (
    recommender.GENRE_WEIGHT,
    recommender.MOOD_WEIGHT,
    recommender.ENERGY_WEIGHT,
)

try:
    for name, profile in profiles.items():
        print(f"\n{name}")

        for label, weights in [
            ("Original", (2.0, 1.0, 1.0)),
            ("Energy-focused", (1.0, 1.0, 2.0)),
        ]:
            (
                recommender.GENRE_WEIGHT,
                recommender.MOOD_WEIGHT,
                recommender.ENERGY_WEIGHT,
            ) = weights

            print(f"  {label}:")
            results = recommender.recommend_songs(profile, songs, k=5)

            for rank, (song, score, _) in enumerate(results, 1):
                print(f"    {rank}. {song['title']} - {score:.2f}")
finally:
    (
        recommender.GENRE_WEIGHT,
        recommender.MOOD_WEIGHT,
        recommender.ENERGY_WEIGHT,
    ) = original_weights
