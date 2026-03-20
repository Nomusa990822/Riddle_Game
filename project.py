import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

RIDDLE_FILE = "riddles.txt"
LEADERBOARD_FILE = "leaderboard.txt"
HISTORY_FILE = "history.txt"
QUESTIONS_PER_ROUND = 10
TIME_LIMIT = 30


def main():
    show_banner()
    loading_animation()

    name = input("Enter your name: ").strip()

    while True:
        difficulty = choose_difficulty()
        riddles = load_riddles(difficulty)

        if len(riddles) < QUESTIONS_PER_ROUND:
            print(
                Fore.RED
                + f"Not enough riddles for this difficulty. Need at least {QUESTIONS_PER_ROUND}."
            )
            return

        questions = random.sample(riddles, QUESTIONS_PER_ROUND)
        score = play_game(questions)

        print(Fore.YELLOW + f"\n🏆 Final Score: {score}/{QUESTIONS_PER_ROUND}")

        update_leaderboard(name, score)
        save_history(name, difficulty, score)
        show_leaderboard()

        if not play_again():
            print(Fore.CYAN + "\nThanks for playing!")
            break


def show_banner():
    print(
        Fore.CYAN
        + """
██████╗ ██╗██████╗ ██████╗ ██╗     ███████╗
██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝
██████╔╝██║██║  ██║██║  ██║██║     █████╗
██╔══██╗██║██║  ██║██║  ██║██║     ██╔══╝
██║  ██║██║██████╔╝██████╔╝███████╗███████╗
╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚══════╝

        RIDDLE QUIZ GAME
"""
    )


def loading_animation():
    print("Loading game", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")


def choose_difficulty():
    while True:
        level = input("Choose difficulty (easy / medium / hard): ").strip().lower()
        if level in ["easy", "medium", "hard"]:
            return level
        print(Fore.RED + "Invalid difficulty. Please choose easy, medium, or hard.")


def load_riddles(level):
    riddles = []

    try:
        with open(RIDDLE_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) != 3:
                    continue

                difficulty, riddle, answer = parts
                if difficulty.lower() == level:
                    riddles.append((riddle.strip(), answer.strip().lower()))

    except FileNotFoundError:
        print(Fore.RED + "Riddle database not found.")
        return []

    return riddles


def play_game(questions):
    score = 0

    for index, (riddle, answer) in enumerate(questions, start=1):
        print(Fore.BLUE + f"\nRiddle {index}/{QUESTIONS_PER_ROUND}: {riddle}")
        print(Fore.CYAN + f"⏳ You have {TIME_LIMIT} seconds.")

        start_time = time.time()
        user_answer = input("Your answer: ").strip().lower()
        end_time = time.time()

        if end_time - start_time > TIME_LIMIT:
            print(Fore.RED + "⏱ Time's up!")
            print("Answer:", answer)
            continue

        if check_answer(user_answer, answer):
            print(Fore.GREEN + "✅ Correct!")
            score += 1
        else:
            print(Fore.RED + "❌ Wrong!")
            print("Answer:", answer)

    return score


def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()


def update_leaderboard(name, score):
    with open(LEADERBOARD_FILE, "a", encoding="utf-8") as file:
        file.write(f"{name},{score}\n")


def show_leaderboard():
    print(Fore.MAGENTA + "\n📊 Leaderboard")

    scores = []

    try:
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 2:
                    continue

                name, score = parts
                try:
                    scores.append((name, int(score)))
                except ValueError:
                    continue

    except FileNotFoundError:
        print("No leaderboard data yet.")
        return

    scores.sort(key=lambda x: x[1], reverse=True)

    if not scores:
        print("No leaderboard data yet.")
        return

    for i, (name, score) in enumerate(scores[:10], start=1):
        print(f"{i}. {name} - {score}")


def save_history(name, difficulty, score):
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"{name},{difficulty},{score}\n")


def play_again():
    answer = input("\nPlay again? (yes/no): ").strip().lower()
    return answer == "yes"


if __name__ == "__main__":
    main()
