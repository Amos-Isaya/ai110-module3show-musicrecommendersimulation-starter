# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

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

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
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

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



