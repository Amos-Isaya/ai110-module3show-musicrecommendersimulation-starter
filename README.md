# 🎵 Music Recommender Simulation

## Project Summary

VibeMatch is a Python music recommender that ranks 18 fictional songs using a listener’s preferred genre, mood, and energy. It displays the top five songs with scores and explanations. I tested four user profiles and changed the scoring weights to explore how design choices affect recommendations.

---

## How The System Works

My recommender will compare songs with a user’s music preferences. Real-world systems can use collaborative filtering, which finds patterns across listeners, or content-based filtering, which uses song characteristics. My version will use content-based filtering.

### Song Information
Each Song will use:
- id: Identifies the song and breaks scoring ties.
- title and artist: Displayed in the recommendations.
- genre: The song’s music category.
- mood: The song’s feeling.
- energy: Its intensity, from 0 to 1.

### User Preferences
The user preferences dictionary will store:
- genre: The user’s favorite genre, such as lofi.
- mood: The user’s preferred mood, such as chill.
- energy: The user’s desired energy level, such as 0.4.

### Scoring and Ranking
The Recommender will give each song:
- 3 points if its genre matches a preferred genre.
- 2 points if its mood matches a preferred mood.
- Energy points calculated as:
  1 - abs(song["energy"] - user_prefs["energy"])

The energy rule rewards songs closer to the user’s desired energy. Genre has the greatest weight because my design prioritizes music category over mood and energy.

The system will sort songs from highest to lowest score and return the requested number of recommendations. Equal scores will be ordered by song ID, lowest first.

Data Flow

Input: User preferences and the 18 songs from the CSV.

Process: Score every song based on genre, mood, and energy similarity.

Output: Sort by highest score and display the top 5 songs. Break ties by song ID, lowest first.

Potential Biases
The system gives genre the most points, so it may overlook songs from other genres that match the user’s mood and energy. It also treats similar moods, such as “happy” and “joyful,” as different. The catalog contains only 18 fictional songs, so its recommendations have limited variety.

---

## Getting Started

### Setup

1. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

2. Activate it on Mac or Linux:

   ```bash
   source .venv/bin/activate
   ```

   On Windows PowerShell, use:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app from the project folder:

   ```bash
   python -m src.main
   ```


### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```text
Loaded songs: 18

Top recommendations:

Midnight Coding - Score: 5.98
Because: Genre match (+3.0); Mood match (+2.0); Energy similarity (+0.98)

Library Rain - Score: 5.95
Because: Genre match (+3.0); Mood match (+2.0); Energy similarity (+0.95)

Focus Flow - Score: 4.00
Because: Genre match (+3.0); Energy similarity (+1.00)

Spacewalk Thoughts - Score: 2.88
Because: Mood match (+2.0); Energy similarity (+0.88)

Letters Unsent - Score: 0.99
Because: Energy similarity (+0.99)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

### Baseline Results for Four Profiles

These results use 3 points for genre, 2 points for mood, and up to 1 point for energy similarity.

```text
=== High-Energy Pop ===
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.9}

1. Sunrise City - Score: 5.92
Because: Genre match (+3.0); Mood match (+2.0); Energy similarity (+0.92)

2. Gym Hero - Score: 3.97
Because: Genre match (+3.0); Energy similarity (+0.97)

3. Rooftop Lights - Score: 2.86
Because: Mood match (+2.0); Energy similarity (+0.86)

4. Storm Runner - Score: 0.99
Because: Energy similarity (+0.99)

5. Forward Together - Score: 0.94
Because: Energy similarity (+0.94)


=== Chill Lofi ===
Preferences: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.4}

1. Midnight Coding - Score: 5.98
Because: Genre match (+3.0); Mood match (+2.0); Energy similarity (+0.98)

2. Library Rain - Score: 5.95
Because: Genre match (+3.0); Mood match (+2.0); Energy similarity (+0.95)

3. Focus Flow - Score: 4.00
Because: Genre match (+3.0); Energy similarity (+1.00)

4. Spacewalk Thoughts - Score: 2.88
Because: Mood match (+2.0); Energy similarity (+0.88)

5. Letters Unsent - Score: 0.99
Because: Energy similarity (+0.99)


=== Deep Intense Rock ===
Preferences: {'genre': 'rock', 'mood': 'intense', 'energy': 0.9}

1. Storm Runner - Score: 5.99
Because: Genre match (+3.0); Mood match (+2.0); Energy similarity (+0.99)

2. Gym Hero - Score: 2.97
Because: Mood match (+2.0); Energy similarity (+0.97)

3. Forward Together - Score: 0.94
Because: Energy similarity (+0.94)

4. Open Sky Festival - Score: 0.93
Because: Energy similarity (+0.93)

5. Sunrise City - Score: 0.92
Because: Energy similarity (+0.92)


=== Edge Case: High-Energy Chill Lofi ===
Preferences: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.95}

1. Midnight Coding - Score: 5.47
Because: Genre match (+3.0); Mood match (+2.0); Energy similarity (+0.47)

2. Library Rain - Score: 5.40
Because: Genre match (+3.0); Mood match (+2.0); Energy similarity (+0.40)

3. Focus Flow - Score: 3.45
Because: Genre match (+3.0); Energy similarity (+0.45)

4. Spacewalk Thoughts - Score: 2.33
Because: Mood match (+2.0); Energy similarity (+0.33)

5. Gym Hero - Score: 0.98
Because: Energy similarity (+0.98)
```
I reduced genre points from 3 to 1.5, kept mood points at 2, and doubled energy similarity points. For Chill Lofi, Spacewalk Thoughts moved above Focus Flow because its matching mood became more valuable than Focus Flow’s matching genre. The same change occurred for the high-energy chill lofi profile. Storm Runner remained first for Intense Rock.

The experiment changed some rankings but did not establish that the recommendations were more accurate. The high-energy chill lofi profile still recommended low-energy songs first because genre and mood together outweighed energy similarity. I chose to retain the original weights as my genre-first design.

### Weight Shift Experimental Output

Genre weight: 1.5
Mood weight: 2.0
Energy similarity weight: 2.0

```text
=== Chill Lofi ===
Preferences: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.4}

1. Midnight Coding - Score: 5.46
Because: Genre match (+1.5); Mood match (+2.0); Energy similarity (+1.96)

2. Library Rain - Score: 5.40
Because: Genre match (+1.5); Mood match (+2.0); Energy similarity (+1.90)

3. Spacewalk Thoughts - Score: 3.76
Because: Mood match (+2.0); Energy similarity (+1.76)

4. Focus Flow - Score: 3.50
Because: Genre match (+1.5); Energy similarity (+2.00)

5. Letters Unsent - Score: 1.98
Because: Energy similarity (+1.98)


=== Deep Intense Rock ===
Preferences: {'genre': 'rock', 'mood': 'intense', 'energy': 0.9}

1. Storm Runner - Score: 5.48
Because: Genre match (+1.5); Mood match (+2.0); Energy similarity (+1.98)

2. Gym Hero - Score: 3.94
Because: Mood match (+2.0); Energy similarity (+1.94)

3. Forward Together - Score: 1.88
Because: Energy similarity (+1.88)

4. Open Sky Festival - Score: 1.86
Because: Energy similarity (+1.86)

5. Sunrise City - Score: 1.84
Because: Energy similarity (+1.84)


=== Edge Case: High-Energy Chill Lofi ===
Preferences: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.95}

1. Midnight Coding - Score: 4.44
Because: Genre match (+1.5); Mood match (+2.0); Energy similarity (+0.94)

2. Library Rain - Score: 4.30
Because: Genre match (+1.5); Mood match (+2.0); Energy similarity (+0.80)

3. Spacewalk Thoughts - Score: 2.66
Because: Mood match (+2.0); Energy similarity (+0.66)

4. Focus Flow - Score: 2.40
Because: Genre match (+1.5); Energy similarity (+0.90)

5. Gym Hero - Score: 1.96
Because: Energy similarity (+1.96)
```

---

## Limitations and Risks

The catalog contains only 18 fictional songs with simulated measurements, so it cannot represent everyone’s musical taste. Exact genre and mood matching can produce repetitive recommendations and overlook similar categories. The system ignores lyrics, language, listening history, and user feedback. Its scores measure agreement with my rules, not the probability that someone will enjoy a song.

---

## Reflection
I learned how song features and user preferences become scores and ranked recommendations. The weight experiment showed that changing the scoring rules can change the order of results without necessarily making them better.

AI helped me design the rules, write code, and troubleshoot errors. I checked the results by running the program with different profiles and running three automated tests. I also learned to verify which file I was editing and save changes before running the program.

My full Model Card and personal reflection are in [model_card.md](model_card.md).




