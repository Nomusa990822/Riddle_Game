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

## 📊 Leaderboard and History

- **leaderboard.txt** stores the top scores of players.
- **history.txt** records each game played, including:
  - player name
  - difficulty level
  - final score

---

## 🧪 Running Tests

To run the automated tests: pytest test_project.py
The tests verify important functions such as answer validation.

---

## 📖 Example Riddle
Riddle: What has keys but can't open locks? Answer: piano

---

## 🔧 Technologies Used

- Python
- File Handling
- Random Module
- Pytest
- GitHub

---

## 🚀 Future Improvements

Possible improvements include:

- Adding **more riddles**
- Implementing **player achievements**
- Adding **difficulty-based scoring**
- Creating a **graphical interface (GUI)**

---

## 👤 Author

Nomusa  
GitHub: https://github.com/Nomusa990822

---

## 📜 License

This project is licensed under the **MIT License**.
