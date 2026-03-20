<h1 align="center">🧩 Riddle Quiz Game</h1>

<p align="center">
Terminal + Web App (Streamlit)
</p>

<p align="center">
  <a href="https://nomusa-riddle-game.streamlit.app/">
    <img src="https://img.shields.io/badge/Play%20Now-Live%20App-success?logo=streamlit">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit">
  <img src="https://img.shields.io/badge/Status-Live-brightgreen">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

---
## Overview

An interactive Python-based riddle game available in two formats:
- Terminal Version – classic command-line gameplay
- Web App Version – built using Streamlit
The game challenges players with randomized riddles, timed responses, and a competitive leaderboard system.

---

## 🎮 Features

- 200+ riddles across 3 difficulty levels
- Easy, Medium, Hard modes
- Randomized questions every round
- 30-second timer per question
- 10 riddles per game session
- Leaderboard system
- Player statistics dashboard (web app)
- Persistent game history
- Play-again functionality
- Colored terminal interface (Colorama)
- Fully deployed web app

---
## 🧩 Game Flow
```
Start Game
   ↓
Enter Name
   ↓
Choose Difficulty
   ↓
Solve 10 Riddles (30 sec each)
   ↓
Score Calculation
   ↓
Leaderboard Update
   ↓
Play Again or Exit
```
---

## 📂 Project Structure
```
riddle-quiz-game
│
├── project.py          # Main game logic
├── riddles.txt         # Database of riddles
├── leaderboard.txt     # Stores player scores
├── history.txt         # Stores previous game results
├── requirements.txt    # Project dependencies
├── test_project.py     # Automated tests
└── README.md           # Project documentation
```
---

## ⚙️ Installation

```
git clone https://github.com/Nomusa990822/Riddle_Game
cd Riddle_Game
pip3 install -r requirements.txt
```

---

## ▶️ Running the Game

1. **Terminal Version**
```
python project.py
```
2. **Streamlit Web App**
```
pip3 install streamlit
python3 -m streamlit run app.py
```

---
## 📝 How to Play

1. Enter your **name**.
2. Choose a **difficulty level**:
   - easy
   - medium
   - hard
3. Answer the riddles before the timer runs out.
4. Earn points for correct answers.
5. Your score will be saved to the **leaderboard**.

---
## 🖥️ App Preview

### Terminal Version
Below is an example of how the game appears when running in the terminal.
```

██████╗ ██╗██████╗ ██████╗ ██╗     ███████╗
██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝
██████╔╝██║██║  ██║██║  ██║██║     █████╗
██╔══██╗██║██║  ██║██║  ██║██║     ██╔══╝
██║  ██║██║██████╔╝██████╔╝███████╗███████╗
╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚══════╝
        RIDDLE QUIZ GAME

Loading game...

Enter your name: X

Choose difficulty (easy / medium / hard): medium

Riddle: What can travel around the world while staying in one corner?

Your answer: stamp

✅ Correct!
```

**Example incorrect answer:**
```
Riddle: What has keys but can't open locks?

Your answer: keyboard

❌ Wrong!
Answer: piano
```
**Example timeout:**
```
Riddle: What gets wetter the more it dries?

Your answer: (after 30 seconds)

⏱ Time's up!
Answer: towel
```
**After 10 riddles, the final score is displayed.**

🏆 Final Score: 3/10

_The score is then automatically saved to the leaderboard_

### Streamlit Web App

---

## 📊 Data Storage

|**File** |**Purpose|
|---------|---------|
|```riddles.txt```|Stores all riddles|
|```leaderboard.txt```|Stores player scores|
|```history.txt```|Stores game sessions|
---

## 🧪 Running Tests

To run the automated tests: ```pytest test_project.py```

The tests verify important functions such as answer validation, input handling and core logic.

---

## 🔧 Technologies Used

- Python
- Colorama (for terminal color)
- Random module (riddle randomization)
- Time module (timer system)
- File handling (persistent leaderboard and history)
- Pytest (unit testing)
- Git & GitHub

---

## 🚀 Future Improvements

Potential enhancements to make the Riddle Game even more engaging and professional:
1. Persistent online leaderboard (database intergration)
2. Expanded Riddle Database/AI-generated riddles
3. Difficulty-Based Scoring
4. Timed Challenge Mode
   Add a mode where players solve as many riddles as possible within a fixed total time.
5. Hint System
   Allow players to request hints that partially reveal answers at the cost of points.
7. Advanced UI/UX enhancements

---

## 👤 Author

Nomusa  
GitHub: ```https://github.com/Nomusa990822```

---

## 📜 License

This project is licensed under the **MIT License**.
