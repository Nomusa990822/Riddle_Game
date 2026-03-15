import random
import time
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

RIDDLE_FILE = "riddles.txt"
LEADERBOARD_FILE = "leaderboard.txt"
HISTORY_FILE = "history.txt"

def load_riddles():
    riddles = {"easy": [], "medium": [], "hard": []}

    with open(RIDDLE_FILE) as file:
        for line in file:
            difficulty, riddle, answer = line.strip().split("|")
            riddles[difficulty].append((riddle, answer))

    return riddles

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game", methods=["POST"])
def game():
    name = request.form["name"]
    difficulty = request.form["difficulty"]

    riddles = load_riddles()

    question = random.choice(riddles[difficulty])

    return render_template(
        "game.html",
        name=name,
        difficulty=difficulty,
        riddle=question[0],
        answer=question[1]
    )

@app.route("/result", methods=["POST"])
def result():
    name = request.form["name"]
    difficulty = request.form["difficulty"]
    correct_answer = request.form["correct"]
    user_answer = request.form["answer"].lower()

    correct = user_answer == correct_answer

    score = 1 if correct else 0

    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{name},{score}\n")

    with open(HISTORY_FILE, "a") as file:
        file.write(f"{name},{difficulty},{score}\n")

    return render_template(
        "result.html",
        correct=correct,
        answer=correct_answer
    )

@app.route("/leaderboard")
def leaderboard():

    scores = []

    with open(LEADERBOARD_FILE) as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) == 2:
                name, score = parts
                scores.append((name, int(score)))

    scores.sort(key=lambda x: x[1], reverse=True)

    return render_template("leaderboard.html", scores=scores[:10])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
