# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0 — Music Recommender Simulation**

VibeFinder 1.0 is a music recommendation system that helps users discover songs based on their favorite genre, preferred mood, and energy level.

---

## 2. Intended Use

VibeFinder is designed to recommend songs that match a user's musical preferences. The system takes information about the user's favorite genre, mood, and desired energy level and generates a ranked list of five songs.

The system assumes that users know what type of music they enjoy and can describe their preferences using these three categories.

This project was created for classroom exploration as part of CodePath AI110. It demonstrates how recommendation algorithms work rather than serving as a fully developed music streaming application.

---

## 3. How the Model Works

VibeFinder uses a rule-based scoring system to determine which songs best match a user's preferences.

Each song receives a score based on three factors:

- **Genre Match (2 points):** If the song matches the user's favorite genre, it receives two points.
- **Mood Match (1 point):** If the song matches the user's preferred mood, it receives one point.
- **Energy Similarity (up to 1 point):** Songs receive more points when their energy level is closer to the user's target energy.

The highest possible score is **4 points**.

After calculating the scores, the system ranks the songs from highest to lowest and recommends the top five.

I improved the starter code by implementing the scoring algorithm, loading song data from a CSV file, ranking recommendations, and generating explanations that show why each song received its score.

Unlike a machine learning model, VibeFinder does not train itself on user behavior. It follows scoring rules defined in the code.

---

## 4. Data

The dataset contains **20 fictional songs**, expanded from the original 10-song starter dataset.

The catalog includes genres such as pop, hip-hop, R&B, rock, jazz, lofi, EDM, soul, reggae, folk, ambient, synthwave, and indie pop.

The songs also represent different moods, including happy, chill, intense, relaxed, focused, and moody.

Each song includes information such as its title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

Although the dataset includes several musical features, the current algorithm only uses genre, mood, and energy to calculate recommendations.

The dataset is limited because it contains only 20 fictional songs. Some genres and moods are represented by just one or two tracks, meaning the system cannot fully represent the variety of real-world musical preferences.

---

## 5. Strengths

One of VibeFinder's biggest strengths is its ability to provide understandable recommendations.

The system works especially well when a user's preferred genre, mood, and energy level are all represented in the dataset.

For example, the Chill Lofi profile received **Library Rain** as its top recommendation with a perfect score of **4.00/4.00** because the song matched all three preferences.

Another strength is transparency. Instead of simply recommending a song, VibeFinder explains which preferences contributed to its score.

The scoring system also provides consistent results, making it easier to understand why one song ranks above another.

---

## 6. Limitations and Bias

One limitation of VibeFinder is that genre has more influence on recommendations than mood or energy.

Because a genre match is worth two points, a song from the user's preferred genre can rank higher than another song that better matches the user's mood.

The system also uses exact genre matches. For example, a user who prefers pop does not automatically receive the genre bonus for indie pop, even though the genres are related.

Another limitation is the small dataset. Users who enjoy genres with fewer available songs may receive less relevant recommendations.

VibeFinder also does not consider listening history, favorite artists, lyrics, cultural influences, or changes in a user's musical taste.

These limitations show how a recommendation system can unintentionally favor certain preferences based on the data and scoring rules used.

---

## 7. Evaluation

I evaluated VibeFinder using three different user profiles to see how the recommendation system responded to different musical preferences.

### Profile 1: High-Energy Pop

- Favorite Genre: Pop
- Preferred Mood: Happy
- Target Energy: 0.80
- Top Recommendation: **Sunrise City — Neon Echo**
- Score: **3.98/4.00**

Sunrise City ranked first because it matched the user's genre and mood, and its energy level of 0.82 was very close to the target.

### Profile 2: Chill Lofi

- Favorite Genre: Lofi
- Preferred Mood: Chill
- Target Energy: 0.35
- Top Recommendation: **Library Rain — Paper Lanterns**
- Score: **4.00/4.00**

Library Rain received a perfect score because its genre, mood, and energy matched the user's preferences.

### Profile 3: Intense Rock

- Favorite Genre: Rock
- Preferred Mood: Intense
- Target Energy: 0.90
- Top Recommendation: **Storm Runner — Voltline**
- Score: **3.99/4.00**

Storm Runner ranked first because it matched the preferred genre and mood, while its energy level was almost identical to the target.

### Testing Results

I ran the program using three user profiles and verified that it generated five ranked recommendations for each.

I also ran the provided automated tests using pytest.

**Results: 2 tests passed, 0 failed.**

One interesting observation was that the Intense Rock profile recommended hip-hop, pop, and EDM songs after Storm Runner. This happened because those songs matched the desired intense mood and high energy, even though their genres were different.

This showed that the algorithm can recommend music outside a user's favorite genre when other preferences align.

---

## 8. Future Work

There are several ways I would improve VibeFinder in the future.

First, I would expand the dataset to include more songs, artists, and genres. This would give users more variety and improve recommendations for less represented musical preferences.

I would also allow users to customize how much importance they place on genre, mood, and energy.

Another improvement would be to incorporate additional song features such as danceability, acousticness, and tempo.

I would also like to build an interactive interface where users could select their preferences and instantly receive recommendations.

Finally, I would explore incorporating user feedback so the system could improve its recommendations based on which songs users actually enjoy.

---

## 9. Personal Reflection

This project helped me better understand how music recommendation systems work behind the scenes.

Before building VibeFinder, I understood that music applications recommended songs based on personal preferences, but this project showed me how those preferences can be translated into numerical scores.

One thing I found interesting was how changing the importance of genre, mood, and energy could influence which songs appeared at the top of the recommendations.

I also learned that a recommendation system does not have to be extremely complicated to produce useful results. Even a simple algorithm can provide personalized recommendations when the scoring rules are clear.

At the same time, the project helped me recognize the limitations of recommendation systems, especially when they rely on small datasets or give certain preferences more importance than others.

Overall, VibeFinder gave me a better understanding of how personalization, algorithms, and data work together in music recommendation applications.

*AI assistance was used during implementation and debugging. The completed program was checked through terminal execution and automated tests.*
