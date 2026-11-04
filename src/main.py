
"""
Music Recommender Simulation
CodePath AI110 - Project 3

This program loads songs from a CSV file,
scores them based on user preferences,
and displays the top 5 recommendations.

It also evaluates the recommender using
three different music taste profiles.
"""

from pathlib import Path
from src.recommender import load_songs, recommend_songs


def display_recommendations(profile_name, user_prefs, songs):
    """Display the top 5 songs for a user profile."""

    print("\n" + "=" * 55)
    print(f"USER PROFILE: {profile_name}")
    print("=" * 55)

    print(f"Favorite Genre: {user_prefs['genre']}")
    print(f"Favorite Mood: {user_prefs['mood']}")
    print(f"Target Energy: {user_prefs['energy']}")

    recommendations = recommend_songs(
        user_prefs,
        songs,
        k=5
    )

    print("\nTOP 5 RECOMMENDATIONS")
    print("-" * 55)

    for rank, (song, score, explanation) in enumerate(
        recommendations, start=1
    ):
        print(f"\n{rank}. {song['title']}")
        print(f"   Artist: {song['artist']}")
        print(f"   Genre: {song['genre']}")
        print(f"   Mood: {song['mood']}")
        print(f"   Energy: {song['energy']:.2f}")
        print(f"   Score: {score:.2f} / 4.00")
        print(f"   Because: {explanation}")

    print("\n" + "=" * 55)


def main() -> None:
    """Run and evaluate the music recommender."""

    # Find the CSV file relative to the project folder.
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "songs.csv"

    print("=" * 55)
    print("       MUSIC RECOMMENDER SIMULATION")
    print("             CodePath AI110")
    print("=" * 55)

    # Load song dataset.
    try:
        songs = load_songs(str(csv_path))

    except FileNotFoundError:
        print("\nERROR: songs.csv was not found.")
        print(f"Expected location: {csv_path}")
        return

    except (ValueError, KeyError) as error:
        print(f"\nERROR loading song data: {error}")
        return

    print(f"\nSuccessfully loaded {len(songs)} songs!")

    if not songs:
        print("No songs available for recommendations.")
        return

    # Three different user profiles for evaluation.
    user_profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8
        },

        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35
        },

        "Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9
        }
    }

    # Generate recommendations for each profile.
    for profile_name, user_prefs in user_profiles.items():
        display_recommendations(
            profile_name,
            user_prefs,
            songs
        )

    print("\nEVALUATION COMPLETE")
    print("All three user profiles have been evaluated.")
    print("Compare their recommendations and scores.")
    print("\nThank you for using Music Recommender!")


if __name__ == "__main__":
    main()
