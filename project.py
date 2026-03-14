import random
import time
import matplotlib.pyplot as plt
from database import init_db, save_score, get_leaderboard

RIDDLE_FILE = "riddles.txt"


def load_riddles():
    riddles = {"easy": [], "medium": [], "hard": []}

    with open(RIDDLE_FILE, "r", encoding="utf-8") as file:
        for line in file:
            difficulty, question, answer = line.strip().split("|")
            riddles[difficulty].append((question, answer))

    return riddles


def ask_riddle(question, answer):

    print("\n🧩", question)

    start = time.time()
    user_answer = input("Your answer: ").strip().lower()
    end = time.time()

    correct = user_answer == answer.lower()
    response_time = round(end - start, 2)

    if correct:
        print("✅ Correct!")
    else:
        print(f"❌ Wrong! Correct answer: {answer}")

    return correct, response_time


def plot_statistics(scores):

    if not scores:
        return

    plt.plot(scores)
    plt.title("Player Performance Over Time")
    plt.xlabel("Game Number")
    plt.ylabel("Score")
    plt.show()


def play():

    riddles = load_riddles()

    print("\n🎮 RIDDLE CHALLENGE")

    name = input("Enter your name: ")

    difficulty = input("Difficulty (easy / medium / hard): ").lower()

    if difficulty not in riddles:
        print("Invalid difficulty")
        return

    questions = random.sample(riddles[difficulty], 5)

    score = 0
    times = []

    for question, answer in questions:

        correct, response_time = ask_riddle(question, answer)

        times.append(response_time)

        if correct:
            score += 1

    print(f"\n🏁 Final Score: {score}/5")

    save_score(name, score)

    leaderboard = get_leaderboard()

    print("\n🏆 Leaderboard")

    for i, player in enumerate(leaderboard[:10], start=1):
        print(f"{i}. {player[0]} - {player[1]}")

    plot = input("\nShow performance graph? (y/n): ")

    if plot.lower() == "y":
        scores = [player[1] for player in leaderboard]
        plot_statistics(scores)


def main():

    init_db()

    while True:

        play()

        again = input("\nPlay again? (y/n): ")

        if again.lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
            
