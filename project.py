import random
import time
import matplotlib.pyplot as plt

RIDDLE_FILE = "riddles.txt"
LEADERBOARD_FILE = "leaderboard.txt"
HISTORY_FILE = "history.txt"


def load_riddles():
    riddles = {"easy": [], "medium": [], "hard": []}

    with open(RIDDLE_FILE, "r") as file:
        for line in file:
            difficulty, question, answer = line.strip().split("|")
            riddles[difficulty].append((question, answer))

    return riddles


def ask_riddle(question, answer):
    print("\nRiddle:")
    print(question)

    start = time.time()
    user_answer = input("Your answer: ").strip().lower()
    end = time.time()

    correct = user_answer == answer.lower()
    response_time = round(end - start, 2)

    if correct:
        print("✅ Correct!")
        return True, response_time
    else:
        print(f"❌ Wrong! Correct answer: {answer}")
        return False, response_time


def update_leaderboard(name, score):

    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{name},{score}\n")


def display_leaderboard():

    print("\n🏆 Leaderboard")

    scores = []

    try:
        with open(LEADERBOARD_FILE, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                scores.append((name, int(score)))
    except FileNotFoundError:
        print("No scores yet.")
        return

    scores.sort(key=lambda x: x[1], reverse=True)

    for i, (name, score) in enumerate(scores[:10], start=1):
        print(f"{i}. {name} - {score}")


def save_history(name, score):

    with open(HISTORY_FILE, "a") as file:
        file.write(f"{name},{score}\n")


def plot_performance():

    scores = []

    try:
        with open(HISTORY_FILE, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                scores.append(int(score))
    except FileNotFoundError:
        print("No history yet.")
        return

    if not scores:
        return

    plt.plot(scores)
    plt.title("Game Performance Over Time")
    plt.xlabel("Game Number")
    plt.ylabel("Score")
    plt.show()


def main():

    riddles = load_riddles()

    print("🧩 Welcome to the Riddle Game!")

    name = input("Enter your name: ")

    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    if difficulty not in riddles:
        print("Invalid difficulty.")
        return

    questions = random.sample(riddles[difficulty], 5)

    score = 0
    times = []

    for question, answer in questions:
        correct, response_time = ask_riddle(question, answer)

        times.append(response_time)

        if correct:
            score += 1

    print(f"\n🎯 Final Score: {score}/5")

    update_leaderboard(name, score)
    save_history(name, score)

    display_leaderboard()

    show_plot = input("\nShow performance graph? (y/n): ")

    if show_plot.lower() == "y":
        plot_performance()


if __name__ == "__main__":
    main()
