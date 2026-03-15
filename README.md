# 🧩 Riddle Quiz Game

An interactive **Python command-line quiz game** where players solve riddles across multiple difficulty levels. The game includes randomized riddles, a timer system, a leaderboard, and persistent game history.

This project was built to practice core programming concepts such as **file handling, functions, randomization, user input validation, and basic game design**.

---

## 🎮 Features

- Three difficulty levels: **Easy, Medium, Hard**
- **Randomized riddles** for a different experience each time
- **Timer-based answering system**
- **Leaderboard tracking** for high scores
- **Game history storage**
- **Play again option**
- **Unit testing using pytest**

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

1. Clone the repository: https://github.com/Nomusa990822/Riddle_Game
2. Navigate into the project folder: cd riddle-quiz-game
3. Install dependencies: pip install -r requirements.txt

---

## ▶️ Running the Game

1. Run the game using: python project.py
2. If Python 3 is required: python3 project.py

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


## 📖 Example Gameplay & Screenshots

**Below is an example of how the game appears when running in the terminal.**

██████╗ ██╗██████╗ ██████╗ ██╗     ███████╗
██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝
██████╔╝██║██║  ██║██║  ██║██║     █████╗
██╔══██╗██║██║  ██║██║  ██║██║     ██╔══╝
██║  ██║██║██████╔╝██████╔╝███████╗███████╗
╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚══════╝

        RIDDLE QUIZ GAME

Loading game...

Enter your name: Nomusa

Choose difficulty (easy / medium / hard): medium

**Each game round contains 5 randomly selected riddles.**

Riddle: What can travel around the world while staying in one corner?

Your answer: stamp

✅ Correct!

**Example incorrect answer:**

Riddle: What has keys but can't open locks?

Your answer: keyboard

❌ Wrong!
Answer: piano

**Example timeout:**

Riddle: What gets wetter the more it dries?

Your answer: (after 60 seconds)

⏱ Time's up!
Answer: towel

**After 5 riddles, the final score is displayed.**

🏆 Final Score: 3/5

The score is then automatically saved to the leaderboard
---

## 📊 Leaderboard and History

- **leaderboard.txt** stores the top 5 scores of players.

  📊 Leaderboard

1. Nomusa - 5
2. Alex - 4
3. Sam - 3
4. Jordan - 2
5. Taylor - 1

   
- **history.txt** records each game played, including:
  - player name
  - difficulty level
  - final score

Nomusa,medium,4
Alex,easy,5
Sam,hard,2

---

## 🎮 Game Flow Diagram

Start Program
      │
      ▼
Display ASCII Banner
      │
      ▼
Loading Animation
      │
      ▼
Enter Player Name
      │
      ▼
Select Difficulty
      │
      ▼
Load Riddles From File
      │
      ▼
Randomly Select 5 Riddles
      │
      ▼
For Each Riddle
      │
      ├─ Start Timer
      │
      ├─ Player Inputs Answer
      │
      ├─ Check If Correct
      │
      └─ Update Score
      │
      ▼
Display Final Score
      │
      ▼
Save Score to Leaderboard
      │
      ▼
Save Game to History File
      │
      ▼
Display Top 5 Leaderboard
      │
      ▼
Play Again?
      │
      ├─ Yes → Restart Game
      │
      └─ No → Exit Program
      
---

## 🧪 Running Tests

To run the automated tests: pytest test_project.py
*The tests verify important functions such as answer validation.*

---

## 🔧 Technologies Used

- **Python**
- **Colorama** (for terminal color)
- **Random module** (riddle randomization)
- **Time module** (timer system)
- **File handling** (persistent leaderboard and history)
- **Pytest** (unit testing)
- **Git & GitHub**

---

## 🚀 Future Improvements

Potential enhancements to make the Riddle Quiz Game even more engaging and professional:
1. **Expanded Riddle Database**
   Increase the dataset to 500–1000+ riddles and organize them by categories.
2. **Difficulty-Based Scoring**
   Assign different points depending on difficulty:
   - Easy = 1 point
   - Medium = 3 points
   - Hard = 5 points
3. **Player Statistics Dashboard**
   Track individual player stats such as:
   - Total riddles solved
   - Accuracy percentage
   - Longest correct-answer streak
4. **Timed Challenge Mode**
   Add a mode where players solve as many riddles as possible within a fixed total time.
5. **Hint System**
   Allow players to request hints that partially reveal answers at the cost of points.
6. **Achievements / Badges**
   Unlock achievements for milestones like:
   - “Riddle Master” – solve 50 riddles
   - “Speed Thinker” – answer under 5 seconds
7. **Improved Terminal UI**
   Use ASCII art, colors, and formatting to make the terminal interface more interactive and visually appealing.
8. **Graphical User Interface (GUI)**
   Create a desktop version using Tkinter or PyQt.
9. **Online Leaderboard**
    Store scores in a database to allow global competition among players.
10. **Web Version**
    Convert the game into a browser-based application using Flask or Django.

---

## 👤 Author

Nomusa  
GitHub: https://github.com/Nomusa990822

---

## 📜 License

This project is licensed under the **MIT License**.
