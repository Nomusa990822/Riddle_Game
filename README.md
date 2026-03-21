<h1 align="center">🧩 Riddle Quiz Game</h1>

<p align="center">
🚀 Terminal + Web App built with Python & Streamlit
</p>

<p align="center">
  <a href="https://nomusa-riddle-game.streamlit.app/">
    <img src="https://img.shields.io/badge/Play%20Now-Live%20App-success?logo=streamlit">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit">
  <img src="https://img.shields.io/badge/Status-Live-brightgreen">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

---

## 🌐 Live Demo

👉 https://nomusa-riddle-game.streamlit.app/

---

## 📌 Overview

The **Riddle Quiz Game** is an interactive Python application designed to challenge users with randomized riddles under time pressure.

This project exists in two versions:

- **Terminal Version** – a command-line game built using core Python  
- **Web Application** – an interactive interface built with Streamlit  

It demonstrates the transition from basic scripting to building and deploying a real-world application.

---

## 🎮 Features

- 200+ riddles across multiple difficulty levels
- Difficulty selection: Easy, Medium, Hard  
- 30-second timer per question  
- 10 riddles per round  
- Randomized questions every game  
- Global leaderboard system  
- Player performance tracking  
- Play-again functionality  
- Styled UI with real-time feedback  

---

## 🧮 Scoring System

| Difficulty | Points per Correct Answer |
|----------|-------------------------|
| Easy     | 2 points                |
| Medium   | 3 points                |
| Hard     | 5 points                |

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

Enter your name:

Choose difficulty (easy / medium / hard):

```

### Web App

![Web App](https://raw.githubusercontent.com/Nomusa990822/Riddle_Game/main/WebAppPic.jpg)

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
Riddle_Game
│
├── app.py              # Streamlit web application
├── project.py          # Terminal version
├── riddles.txt         # Riddle dataset (200+ riddles)
├── leaderboard.txt     # Stores scores
├── history.txt         # Stores gameplay history
├── requirements.txt    # Dependencies
├── test_project.py     # Unit tests
└── README.md
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

## 🧪 Testing

To run the automated tests: ```pytest test_project.py```

Tests cover: 
- Answer validation
- Case-insensitive input handling
- Whitespace handling
- Difficulty-based scoring

---

## 🔧 Technologies Used

- Python
- Colorama (for terminal color)
- Random module (riddle randomization)
- Time module (timer system)
- File handling (persistent leaderboard and history)
- Pytest (unit testing)
- Git & GitHub
- Streamlit

---

## 🚀 Future Improvements

The current version of the Riddle Quiz Game provides a strong foundation, and several enhancements can be implemented to evolve it into a more robust and scalable application:

### 🌍 Backend & Data
- Integrate a database (SQLite, Firebase, or PostgreSQL) for persistent and reliable leaderboard storage  
- Enable real-time leaderboard updates across multiple users  
- Store user profiles and long-term performance tracking  

### 🎮 Gameplay Enhancements
- Add difficulty-based timer adjustments  
- Introduce bonus points for faster answers  
- Implement streak-based scoring or achievements system  
- Add hints system for challenging riddles  

### 🎨 User Experience (UI/UX)
- Improve mobile responsiveness and layout  
- Add animations and transitions for better interactivity  
- Introduce dark/light mode toggle  
- Add sound effects for correct/incorrect answers  

### 🤖 Advanced Features
- Integrate AI to generate new riddles dynamically  
- Add multiplayer or competitive mode  
- Implement user authentication (login/signup system)  
- Add categories (logic, math, wordplay, etc.)  

### 📈 Performance & Deployment
- Optimize app performance for faster loading  
- Improve error handling and logging  
- Deploy using a scalable cloud backend

---

## ⚠️ Limitations

- The application supports multiple users accessing the game simultaneously, as it is deployed online.

- However, the current implementation uses local file storage (`leaderboard.txt` and `history.txt`), which means:
  - Data is not guaranteed to be consistent across multiple users
  - Simultaneous writes may cause minor inconsistencies
  - Data may reset if the app restarts

- For a production-level system, a database (e.g., SQLite, Firebase, or PostgreSQL) would be used to ensure reliable, real-time data storage and scalability.

---

## 👤 Author

Nomusa Shongwe

GitHub: ```https://github.com/Nomusa990822```

---

## 📜 License

This project is licensed under the **MIT License**.
