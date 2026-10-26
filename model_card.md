# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatch 1.0

---

## 2. Intended Use  

VibeMatch suggests songs based on a user’s preferred genre, mood, and energy. It is a classroom simulation for learning how recommendation systems work. It assumes users can describe these preferences. It is not designed for a real streaming service or for making reliable predictions about everyone’s music taste.

---

## 3. How the Model Works  

My recommender compares each song’s genre, mood, and energy with the user’s preferences. A matching genre earns 3 points, and a matching mood earns 2 points. Energy adds up to 1 point: the closer the song’s energy is to the user’s desired level, the more points it earns.

The program scores every song, sorts them from highest to lowest score, and returns the requested number of recommendations. Songs with equal scores are ordered by song ID, lowest first. Each recommendation includes an explanation showing where its points came from.

I replaced the empty starter functions with CSV loading, numerical conversions, weighted scoring, and ranking. The terminal version now loads 18 songs and displays the top 5 recommendations with scores and reasons.

---

## 4. Data  

The catalog contains 18 fictional songs: 10 starter songs and 8 AI-generated additions. The additions introduced genres such as Afrobeats, classical, hip hop, gospel, reggae, country, R&B, and EDM.

Each song includes its title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The current scoring uses only genre, mood, and energy. The numerical values are simulated, and the catalog does not represent the full variety of music or listeners. 

---

## 5. Strengths  

The system gives understandable results for the profiles tested. Sunrise City ranked first for happy pop, Midnight Coding for chill lofi, and Storm Runner for intense rock. Its explanations show which preferences earned points. The separate scoring function also makes the rules easy to change and compare.

---

## 6. Limitations and Bias 

The system strongly favors exact genre and mood matches, which can create repetitive recommendations. In the high-energy chill lofi experiment, low-energy lofi songs stayed first even though the user requested energy of 0.95. The small catalog contains three lofi songs but only one rock song, so some preferences have more matching options than others. It also treats similar moods such as “happy” and “joyful” as different and uses fictional song measurements rather than real audio analysis. 

---

## 7. Evaluation  

I ran four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and High-Energy Chill Lofi. Their baseline first choices were Sunrise City, Midnight Coding, Storm Runner, and Midnight Coding, respectively. I also ran three automated tests covering pop ranking, lofi ranking, and nonempty explanations; all passed before the weight experiment.

Comparing the profiles:
- Pop versus Lofi: Sunrise City changed to Midnight Coding because the preferred genre, mood, and energy changed.
- Pop versus Rock: Sunrise City changed to Storm Runner despite both profiles targeting energy of 0.9, showing the influence of genre and mood.
- Pop versus High-Energy Chill Lofi: Midnight Coding replaced Sunrise City even with a high energy target because lofi and chill matches earned more points.
- Lofi versus Rock: The recommendations shifted from calmer lofi songs toward intense rock and other energetic tracks.
- Lofi versus High-Energy Chill Lofi: The first four songs stayed in the same order, but Gym Hero replaced Letters Unsent in fifth place because of its higher energy.
- Rock versus High-Energy Chill Lofi: Storm Runner changed to Midnight Coding because the genre and mood preferences differed.
For the weight experiment, I halved genre points to 1.5, kept mood at 2, and doubled energy similarity. Spacewalk Thoughts moved above Focus Flow for both lofi profiles, while the first-place songs stayed unchanged in the three experimental outputs reviewed. This showed sensitivity to weights, but did not prove improved accuracy. I restored the original scoring afterward

---

## 8. Future Work  

Let users select multiple genres and moods.
Recognize similar mood labels, such as “happy” and “joyful.”
Add more varied songs and introduce diversity among the top recommendations.

---

## 9. Personal Reflection  

My biggest learning moment was seeing how song information becomes a score and then a ranked recommendation. I initially found the numerical features confusing, but comparing song energy with the user’s preferred energy helped me understand their purpose. Simple matching rules produced results that looked reasonable from the song descriptions, even without training a machine-learning model.

AI helped me plan the scoring, expand the fictional dataset, write code, and troubleshoot errors. I still needed to check which file the code belonged in, save my changes, run the program, and inspect the results. The weight experiment showed me that changing the rules changes what the system prioritizes, but different results are not automatically better. Next, I would add multiple preferences and improve recommendation variety.