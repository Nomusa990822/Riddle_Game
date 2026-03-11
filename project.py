import random
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

RIDDLE_FILE = "riddles.txt"
LEADERBOARD_FILE = "leaderboard.txt"
HISTORY_FILE = "history.txt"

# --- Load riddles safely ---
def load_riddles(level):
    riddles = []
    if not os.path.exists(RIDDLE_FILE):
        print(Fore.RED + "Riddle database not found.")
        return riddles
    with open(RIDDLE_FILE, "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) != 3:
                continue
            difficulty, riddle, answer = parts
            if difficulty.lower() == level.lower():
                riddles.append((riddle, answer))
    return riddles

# --- Check answer ---
def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()

# --- Update leaderboard ---
def update_leaderboard(name, score):
    leaderboard = []
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            for line in file:
                try:
                    player, points = line.strip().split(",")
                    leaderboard.append((player, int(points)))
                except:
                    continue
    leaderboard.append((name, score))
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    with open(LEADERBOARD_FILE, "w") as file:
        for player, points in leaderboard[:10]:  # Keep top 10
            file.write(f"{player},{points}\n")
    return leaderboard[:10]

# --- Update history ---
def update_history(name, difficulty, score):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{name},{difficulty},{score}\n")

# --- Play a game session ---
def play_game(name, difficulty):
    riddles = load_riddles(difficulty)
    if len(riddles) < 5:
        print(Fore.RED + "Not enough riddles for this difficulty.")
        return 0
    random.shuffle(riddles)
    score = 0
    for i, (riddle, answer) in enumerate(riddles[:5], 1):  # 5 riddles per round
        print(Fore.CYAN + f"Riddle {i}: {riddle}")
        start_time = time.time()
        user_answer = input("Your answer: ")
        end_time = time.time()
        if end_time - start_time > 60:  # 60 sec timer
            print(Fore.YELLOW + "Time's up!")
        elif check_answer(user_answer, answer):
            print(Fore.GREEN + "Correct!")
            score += 1
        else:
            print(Fore.RED + f"Wrong! Correct answer: {answer}")
    print(Fore.MAGENTA + f"\n{name}, your score this round: {score}/5")
    update_history(name, difficulty, score)
    leaderboard = update_leaderboard(name, score)
    print(Fore.BLUE + "\n--- Leaderboard (Top 10) ---")
    for i, (player, points) in enumerate(leaderboard, 1):
        print(Fore.BLUE + f"{i}. {player} - {points}")
    return score

# --- Main function ---
def main():
    print("\n==============================")
    print("      RIDDLE QUIZ GAME        ")
    print("==============================\n")
    name = input("Enter your name: ").strip()
    
    while True:
        difficulty = input("Choose difficulty (easy / medium / hard): ").strip().lower()
        if difficulty in ["easy", "medium", "hard"]:
            break
        print("Invalid difficulty. Try again.")
    
    play_game(name, difficulty)

    while True:
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again == "y":
            while True:
                difficulty = input("Choose difficulty (easy / medium / hard): ").strip().lower()
                if difficulty in ["easy", "medium", "hard"]:
                    break
                print("Invalid difficulty. Try again.")
            play_game(name, difficulty)
        else:
            print("\nThanks for playing! Goodbye.")
            break

# --- Run main ---
if __name__ == "__main__":
    main()
