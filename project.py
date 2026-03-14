import random
import time
import os

RIDDLE_FILE = "riddles.txt"
LEADERBOARD_FILE = "leaderboard.txt"
HISTORY_FILE = "history.txt"


def load_riddles():
    """
    Load riddles from riddles.txt and organize them by difficulty.
    """
    riddles = {"easy": [], "medium": [], "hard": []}

    if not os.path.exists(RIDDLE_FILE):
        return riddles

    with open(RIDDLE_FILE, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("|")

            if len(parts) != 3:
                continue

            difficulty, question, answer = parts

            difficulty = difficulty.lower()

            if difficulty in riddles:
                riddles[difficulty].append((question, answer))

    return riddles


def ask_question(question, answer, time_limit=20):
    """
    Ask the user a riddle and check if the answer is correct.
    Includes a timer.
    """

    print("\n🧩 Riddle:")
    print(question)

    start_time = time.time()

    user_answer = input("Your answer: ").strip().lower()

    elapsed_time = time.time() - start_time

    if elapsed_time > time_limit:
        print("⏰ Time's up!")
        return False

    if user_answer == answer.lower():
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! The correct answer was: {answer}")
        return False


def update_leaderboard(name, score):
    """
    Save player score to leaderboard.txt
    """

    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{name},{score}\n")


def display_leaderboard():
    """
    Display top scores from leaderboard.txt
    """

    print("\n🏆 Leaderboard")

    if not os.path.exists(LEADERBOARD_FILE):
        print("No scores yet.")
        return

    scores = []

    with open(LEADERBOARD_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) != 2:
                continue

            name, score = parts
            scores.append((name, int(score)))

    scores.sort(key=lambda x: x[1], reverse=True)

    for i, (name, score) in enumerate(scores[:10], start=1):
        print(f"{i}. {name} - {score}")


def save_history(name, difficulty, score):
    """
    Save game history
    """

    with open(HISTORY_FILE, "a") as file:
        file.write(f"{name},{difficulty},{score}\n")


def play_game():
    """
    Run a single game session.
    """

    riddles = load_riddles()

    print("\n🧩 Welcome to the Riddle Quiz Game!")

    name = input("Enter your name: ").strip()

    difficulty = input("Choose difficulty (easy / medium / hard): ").lower()

    if difficulty not in riddles:
        print("Invalid difficulty.")
        return

    if len(riddles[difficulty]) == 0:
        print("No riddles available for this difficulty.")
        return

    questions = random.sample(
        riddles[difficulty], min(5, len(riddles[difficulty]))
    )

    score = 0

    for question, answer in questions:

        correct = ask_question(question, answer)

        if correct:
            score += 1

    print(f"\n🎯 Final Score: {score}/5")

    update_leaderboard(name, score)

    save_history(name, difficulty, score)

    display_leaderboard()


def main():
    """
    Main game loop.
    """

    while True:

        play_game()

        again = input("\nPlay again? (yes/no): ").lower()

        if again != "yes":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
