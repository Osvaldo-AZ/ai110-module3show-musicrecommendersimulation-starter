# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
Music Muse

---

## 2. Intended Use  
Tries to recommend music based on user preferences.Mostly based on Genre and Mood. Built mostly for classroom exploration. 

---

## 3. How the Model Works  
The recommender is like a matchmaker for music. It gives each song a score out of 1.0 based on how well it matches your taste.

**What gets scored:**
- **Genre** (30% importance)
- **Energy** (20% importance)
- **Valence** (15% importance)
- **Acousticness** (10% importance)

**How it works:**
For each song, the model checks: "Does it match their genre?" (yes/no). Then it measures how close the song's energy, mood, and acoustic qualities are to what the user wants. Songs that are *exactly* what you want get higher scores; songs that are way off get lower scores. Finally, it ranks all songs by score and recommends the top 5.

---

## 4. Data  

The dataset has 18 songs. It's a mix of different genres and moods to test the recommender. The original data set was not changed, only added to. 

Genres included: pop, rock, lofi, ambient, jazz, synthwave, indie pop, country, hip-hop, classical, r&b, metal, folk, electronic, blues.

Moods included: happy, chill, intense, relaxed, moody, focused, energetic, melancholic, romantic, angry, dreamy, uplifting.

The dataset is small and meant for classroom testing, not real recommendations. It doesn't have much depth in any one genre. For a real recommender, you'd want thousands of songs with more diverse moods and subgenres.

---

## 5. Strengths  

The system works best for users with clear, mainstream tastes. Pop fans, lofi listeners, and rock fans all get solid recommendations that make sense.

If you flag a favorite genre, the system heavily prioritizes songs in that genre. This works great for people who know what they like.

A user who wants high-energy songs will get high-energy songs. A user who likes acoustic music will get acoustic tracks. The proximity scoring (squared distance) means small gaps are forgiven, but big mismatches hurt.

When I tested the Chill Lofi profile, it got quiet, acoustic tracks. The High-Energy Pop profile got upbeat, produced songs, which felt right. 

---

## 6. Limitations and Bias 

The primary weakness to this system is that Genre and Mood hold 0.55 of the weight budget. This means that a song that matches genre and mood but nothing else, will always outrank a numerically perfect song in the wrong genre. Users are structurally locked into their declaured genre, and the system can't surface a cross-genre discovery.
 

---

## 7. Evaluation  

To evaluate the recommender, 8 user profiles were tested: three normal profiles (High-Energy Pop, Chill Lofi, Deep Intense Rock) and five adversarial edge cases (Sad Raver, Classical Rage, Loud Acoustic Fan, The Minimalist, and Dancefloor Obsessed).

For the normal profiles the results felt reasonable. But the edge cases were a different story. The Classical Rage profile had no songs matching both its genre and mood, so the ranking fell back entirely on numeric proximity — the top result ended up being a metal track, which happened to share the high-energy and low-valence targets even though it shared no declared genre or mood.

The most surprising result came from temporarily commenting out the mood check. Rankings shifted noticeably for profiles where mood was doing heavy lifting (such as Chill Lofi), but barely changed for profiles where the genre match was already strong enough to dominate. This showed that mood and genre are not independent — when one is strong, the other becomes less decisive.

---

## 8. Future Work  

**Add diversity to the top 5.** Currently, if you get high scores, you might get 5 almost-identical songs. I'd add a filter that ensures the top 5 don't all have similar artists, tempos, or energy levels. More variety = more interesting discoveries.

**Improve explanations.** Right now the system says "matches your favorite genre" or "energy is close." I'd add *why* a song might surprise you ("This usually isn't your genre, but the mood matches") to help users discover new music intentionally.

---

## 9. Personal Reflection  

I learned about how weights can lock people into a box. While 30% doesn't seem like a lot, it definitely narrows discovery. 

I was able to use Claude Code easily for the bulk of the implementation. I was surprised that it was not necessarily implementing in the most Pythonic way. 

The most surprising discovery was that mood and genre aren't independent. When the mood feature was disabled, results barely shifted with songs shifting a bit. 

I understand a bit more on why YouTube Music feels like it just recommends the same songs over and over. 

One thing I would try next would be to rebalancing the weights to see if I can get more accurate recommendations. And to see if the edge cases improve without breaking the normal cases. 
