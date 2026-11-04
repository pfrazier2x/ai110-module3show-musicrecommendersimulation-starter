# 🎵 Music Recommender Simulation

## Project Summary

This project is a Python-based music recommendation system that helps users discover songs based on their music preferences. The system uses content-based filtering to compare a user's favorite genre, mood, and energy level with songs in a dataset.

Each song receives a score based on how closely it matches the user's preferences. The songs with the highest scores are recommended first. The goal of this project is to understand how platforms like Spotify use data and algorithms to make personalized music recommendations.

## How The System Works

My music recommender uses content-based filtering. Instead of looking at what other people listen to, the system focuses on the characteristics of each song and compares them to the user's preferences.

### Song Features

Each song in the dataset includes information such as:

- **Title:** The name of the song.
- **Artist:** The person or group performing the song.
- **Genre:** The type of music, such as pop, hip-hop, rock, or R&B.
- **Mood:** The feeling of the song, such as happy, chill, or sad.
- **Energy:** A number between 0.0 and 1.0 that represents how energetic a song is.
- **Tempo:** The speed of the song measured in beats per minute (BPM).

### User Profile

The user profile stores the listener's music preferences:

- Favorite genre
- Favorite mood
- Target energy level

For example, a user might prefer hip-hop music with a chill mood and an energy level of 0.6.

### Scoring Algorithm

The recommender calculates a score for each song using a weighted scoring system.

- Genre match: +2.0 points
- Mood match: +1.0 point
- Energy similarity: Up to +1.0 point

Energy similarity is calculated using:

`1.0 - abs(song_energy - target_energy)`

This formula rewards songs with energy levels closer to the user's preference.

For example, if a user prefers hip-hop, chill music, and an energy level of 0.6, a song matching both genre and mood with an energy level of 0.7 would receive:

- Genre: 2.0
- Mood: 1.0
- Energy: 0.9
- Total Score: 3.9

### Recommendation Process

1. Load song information from `data/songs.csv`.
2. Read the user's music preferences.
3. Compare each song against the user's profile.
4. Calculate a score for each song.
5. Sort the songs from highest to lowest score.
6. Recommend the top 5 songs.
7. Display each recommendation with its score and the reasons it was selected.

### Data Flow

User Preferences → Song Dataset → Scoring Algorithm → Song Ranking → Top 5 Recommendations

This approach is simple and easy to understand, but it can sometimes recommend too many songs from the same genre.

---

## Getting Started

### Setup

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd ai110-module3show-musicrecommendersimulation-starter
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
```

Activate the virtual environment.

Mac or Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python -m src.main
```

### Running Tests

Run the tests using:

```bash
pytest
```

Additional tests can be added in `tests/test_recommender.py`.

---

## Sample Recommendation Output

The program will display the top recommended songs, their scores, and the reasons they were selected.

**To be completed after running the program.**

```text
User Profile: To be determined

Top 5 Recommendations:

[Paste actual terminal output here]
```

---

## Experiments You Tried

To evaluate the recommender, I will test it with different user preferences and compare how the recommendations change.

### Experiment 1: Different User Profiles

The recommender will be tested using three profiles:

1. High-Energy Pop: Pop music with a happy mood and high energy.
2. Chill Lofi: Lofi music with a chill mood and low energy.
3. Intense Rock: Rock music with an intense mood and high energy.

I will compare the top five recommendations for each profile to see how the algorithm responds to different musical preferences.

### Experiment 2: Changing Feature Weights

I will test how changing the importance of genre and energy affects the recommendations.

The original scoring system gives genre matches 2.0 points and energy similarity up to 1.0 point.

For the experiment, I will reduce the genre weight to 1.0 and increase the energy similarity weight to 2.0.

**Results:** To be completed after running the experiments.

---

## Limitations and Risks

My music recommendation system has several limitations.

- **Small Dataset:** The system only recommends songs included in its CSV file.
- **Limited Features:** It mainly focuses on genre, mood, and energy instead of lyrics, listening history, or other musical characteristics.
- **Filter Bubbles:** The algorithm may repeatedly recommend songs from the same genre instead of introducing users to different types of music.
- **No User Feedback:** The system does not automatically learn from songs users like or skip.
- **Scoring Bias:** Giving genre more points than mood or energy may cause the system to favor certain songs even when other songs match the user's overall vibe better.

These limitations show how even a simple recommendation algorithm can influence what music users discover.

---

## Reflection

This project is helping me understand how recommendation systems turn data into personalized suggestions. Before working on this project, I knew that platforms like Spotify recommended music based on listening habits, but I did not fully understand how individual song features could be used to calculate recommendations. Building a scoring system demonstrates how genre, mood, and energy can be combined to rank songs.

I am also learning that the way an algorithm is designed can influence its results. For example, giving genre more importance than mood could cause the system to overlook songs that a user might actually enjoy. AI tools can help with designing the algorithm and debugging the code, but I still need to test the recommendations and verify that the results make sense.

I will update this reflection after completing the implementation and experiments.

For more information about the system's evaluation and limitations, see the [Model Card](model_card.md).
