# 🎵 Music Recommender Simulation — VibeFinder 1.0

## Project Summary

VibeFinder 1.0 is a Python-based music recommendation system that helps users discover songs based on their musical preferences. The system uses content-based filtering to compare a user's favorite genre, preferred mood, and target energy level with songs in a dataset.

Each song receives a score based on how closely it matches the user's preferences. The songs with the highest scores are recommended first.

The goal of this CodePath AI110 project is to understand how music recommendation platforms can use data and algorithms to create personalized suggestions.

## How the System Works

VibeFinder uses a rule-based, content-based recommendation approach. Instead of looking at what other people listen to, the system focuses on the characteristics of each song and compares them with the user's preferences.

### Song Features

The dataset contains the following information for each song:

- **ID:** A unique identifier for each song.
- **Title:** The name of the song.
- **Artist:** The person or group performing the song.
- **Genre:** The type of music, such as pop, hip-hop, rock, or R&B.
- **Mood:** The feeling of the song, such as happy, chill, or intense.
- **Energy:** A value between 0.0 and 1.0 representing how energetic a song is.
- **Tempo:** The song's speed in beats per minute (BPM).
- **Valence:** A numerical measure associated with the song's musical positivity.
- **Danceability:** A numerical measure of how suitable a song is for dancing.
- **Acousticness:** A numerical measure of the song's acoustic characteristics.

The current scoring algorithm uses genre, mood, and energy. The remaining features are stored for possible future improvements.

### User Profile

The user profile stores three main listening preferences:

- Favorite genre
- Favorite mood
- Target energy level

For example, a user might prefer hip-hop music with a chill mood and an energy level of 0.6.

### Scoring Algorithm

The recommender calculates a score for each song using a weighted scoring system.

| Feature | Maximum Points |
|---|---:|
| Genre match | 2.0 |
| Mood match | 1.0 |
| Energy similarity | 1.0 |
| **Total** | **4.0** |

Energy similarity is calculated using:

`1.0 - abs(song_energy - target_energy)`

This formula rewards songs whose energy levels are closer to the user's preference.

For example, if a user prefers hip-hop, chill music, and an energy level of 0.6, a song matching both genre and mood with an energy level of 0.7 would receive:

- Genre: 2.0
- Mood: 1.0
- Energy: 0.9
- **Total Score: 3.9/4.0**

### Recommendation Process

1. Load song information from `data/songs.csv`.
2. Read the user's music preferences.
3. Compare each song against the user's profile.
4. Calculate a score for each song.
5. Sort the songs from highest to lowest score.
6. Recommend the top five songs.
7. Display each recommendation with its score and an explanation.

### Data Flow

**User Preferences → Song Dataset → Scoring Algorithm → Song Ranking → Top 5 Recommendations**

This approach is simple and explainable, but it may prioritize songs from the same genre because genre receives the highest weight.

---

## Getting Started

### Setup

**1. Clone the repository**

```bash
git clone https://github.com/pfrazier2x/ai110-module3show-musicrecommendersimulation-starter.git
cd ai110-module3show-musicrecommendersimulation-starter
```

**2. Create a virtual environment (optional)**

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

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Run the application**

```bash
python -m src.main
```

The application loads the dataset and displays recommendations for three example user profiles.

### Running Tests

Run the tests using:

```bash
python -m pytest
```

The two provided automated tests passed successfully during evaluation.

**Test Results: 2 passed, 0 failed.**

Additional tests can be added to `tests/test_recommender.py`.

---

## Sample Recommendation Output

The recommender was successfully tested with a dataset of **20 fictional songs**.

### Profile 1: High-Energy Pop

**Preferences:**
- Genre: Pop
- Mood: Happy
- Target Energy: 0.80

| Rank | Song | Artist | Score |
|---|---|---|---:|
| 1 | Sunrise City | Neon Echo | 3.98 |
| 2 | Gym Hero | Max Pulse | 2.87 |
| 3 | Rooftop Lights | Indigo Parade | 1.96 |
| 4 | Electric Nights | Future Pulse | 1.92 |
| 5 | Golden Hour | Soul Avenue | 1.78 |

**Top recommendation:** Sunrise City received a score of 3.98/4.00 because it matched the user's preferred genre and mood, while its energy level of 0.82 was close to the target of 0.80.

### Profile 2: Chill Lofi

**Preferences:**
- Genre: Lofi
- Mood: Chill
- Target Energy: 0.35

| Rank | Song | Artist | Score |
|---|---|---|---:|
| 1 | Library Rain | Paper Lanterns | 4.00 |
| 2 | Midnight Coding | LoRoom | 3.93 |
| 3 | Focus Flow | LoRoom | 2.95 |
| 4 | Spacewalk Thoughts | Orbit Bloom | 1.93 |
| 5 | Ocean Breeze | Island Vibes | 1.85 |

**Top recommendation:** Library Rain received a perfect score of 4.00/4.00 because its genre, mood, and energy matched the user's preferences.

### Profile 3: Intense Rock

**Preferences:**
- Genre: Rock
- Mood: Intense
- Target Energy: 0.90

| Rank | Song | Artist | Score |
|---|---|---|---:|
| 1 | Storm Runner | Voltline | 3.99 |
| 2 | Victory Lap | Metro Kings | 2.00 |
| 3 | Gym Hero | Max Pulse | 1.97 |
| 4 | Fast Lane | Turbo Wave | 1.95 |
| 5 | Electric Nights | Future Pulse | 0.98 |

**Top recommendation:** Storm Runner received a score of 3.99/4.00 because it matched the preferred genre and mood, and its energy level of 0.91 was extremely close to the target.

---

## Experiments and Evaluation

### Experiment 1: Different User Profiles

I tested VibeFinder using three different user profiles to evaluate how the recommendations changed based on musical preferences.

| User Profile | Top Recommendation | Score |
|---|---|---:|
| High-Energy Pop | Sunrise City | 3.98/4.00 |
| Chill Lofi | Library Rain | 4.00/4.00 |
| Intense Rock | Storm Runner | 3.99/4.00 |

**Findings:**

The algorithm successfully identified songs that closely matched the preferred genre, mood, and energy level for all three profiles.

One interesting result was that the Intense Rock profile received recommendations from hip-hop, pop, and EDM genres after its top rock recommendation. These songs ranked highly because they matched the user's intense mood and high energy level.

This demonstrated that VibeFinder can recommend songs outside a user's favorite genre when other musical characteristics align.

### Experiment 2: Changing Feature Weights

The original scoring system gives genre matches 2.0 points, mood matches 1.0 point, and energy similarity up to 1.0 point.

A proposed experiment is to reduce the genre weight to 1.0 and increase the energy similarity weight to 2.0.

**Original weights:**
- Genre: 2.0
- Mood: 1.0
- Energy: 1.0

**Alternative weights:**
- Genre: 1.0
- Mood: 1.0
- Energy: 2.0

This change would give energy similarity more influence on the ranking and reduce the importance of exact genre matches.

**Status:** This alternative-weight experiment has been proposed but has not yet been executed or measured. The current implementation uses the original weights.

---

## Limitations and Risks

VibeFinder has several limitations.

- **Small Dataset:** The system only recommends songs included in its 20-song CSV file.
- **Limited Features:** It focuses on genre, mood, and energy rather than lyrics, listening history, or other musical characteristics.
- **Filter Bubbles:** The algorithm may repeatedly recommend similar songs instead of encouraging broader music discovery.
- **No User Feedback:** The system does not automatically learn from songs users like or skip.
- **Scoring Bias:** Giving genre more points than mood or energy may cause the system to favor exact genre matches.
- **Exact Genre Matching:** Related genres, such as pop and indie pop, are treated as different categories.
- **Limited Representation:** Some genres and moods have fewer songs in the dataset than others.

These limitations demonstrate how the design of a recommendation algorithm can influence which songs users discover.

---

## Reflection

This project helped me understand how recommendation systems turn data into personalized suggestions. Before working on VibeFinder, I knew that music platforms recommended songs based on listening habits, but I did not fully understand how individual song features could be used to calculate recommendations.

Building the scoring algorithm helped me see how genre, mood, and energy can be combined to rank songs. It also showed me how changing the importance of different features can influence which recommendations appear first.

One thing I found interesting was how the Intense Rock profile received recommendations from genres outside rock because those songs still matched the desired mood and energy level. This demonstrated that recommendation systems can identify similarities between songs even when they belong to different genres.

I also learned the importance of debugging and testing. During development, I encountered issues with CSV formatting, Python imports, and GitHub synchronization. Resolving these problems helped me better understand how the different parts of a Python project work together.

AI tools assisted with implementation and debugging, while terminal execution and automated tests were used to verify the program's behavior.

Overall, this project gave me a better understanding of how recommendation systems use algorithms to personalize content and how the quality of recommendations depends on both the data and the scoring rules.

---

## Model Card

For more information about the system's intended use, evaluation, strengths, limitations, and future improvements, see the [Model Card](model_card.md).
