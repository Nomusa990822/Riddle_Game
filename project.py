import random
import time
import os

# Load riddles from file
def load_riddles(difficulty):
    riddles = []
    with open("riddles.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) != 3:
                continue
            riddle_diff, riddle, answer = parts
            if riddle_diff.lower() == difficulty.lower():
                riddles.append((riddle, answer))
    if len(riddles) < 1:
        print("Not enough riddles for this difficulty.")
        exit()
    return riddles

# Update leaderboard
def update_leaderboard(name, score):
    leaderboard = []
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) != 2:
                    continue
                leaderboard.append((parts[0], int(parts[1])))
    leaderboard.append((name, score))
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    leaderboard = leaderboard[:10]  # top 10
    with open("leaderboard.txt", "w", encoding="utf-8") as f:
        for entry in leaderboard:
            f.write(f"{entry[0]}|{entry[1]}\n")

# Show leaderboard
def show_leaderboard():
    print("\n--- LEADERBOARD ---")
    if not os.path.exists("leaderboard.txt"):
        print("No leaderboard yet!")
        return
    with open("leaderboard.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 2:
                print(f"{parts[0]}: {parts[1]} points")

# Save game history
def save_history(name, difficulty, score):
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"{name}|{difficulty}|{score}\n")

# Ask riddles with timer
def play_riddles(riddles):
    score = 0
    # Play 5 random riddles per game
    for riddle, answer in random.sample(riddles, min(5, len(riddles))):
        print("\nRiddle:", riddle)
        start_time = time.time()
        user_answer = input("Your answer: ").strip().lower()
        end_time = time.time()
        elapsed = end_time - start_time
        if elapsed > 20:  # 20-second timer per riddle
            print("Time's up!")
        elif user_answer == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer was: {answer}")
    return score

def show_banner():
    print(Fore.CYAN + """
██████╗ ██╗██████╗ ██████╗ ██╗     ███████╗
██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝
██████╔╝██║██║  ██║██║  ██║██║     █████╗
██╔══██╗██║██║  ██║██║  ██║██║     ██╔══╝
██║  ██║██║██████╔╝██████╔╝███████╗███████╗
╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚══════╝
""")
print("RIDDLE QUIZ GAME\nLoading game...\n")

    name = input("Enter your name: ").strip()
    difficulty = input("Choose difficulty (easy / medium / hard): ").strip().lower()

    riddles = load_riddles(difficulty)
    score = play_riddles(riddles)
    print(f"\n{name}, your score is: {score}")

    update_leaderboard(name, score)
    save_history(name, difficulty, score)

    show_leaderboard()

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("\nThanks for playing!")

if __name__ == "__main__":
    main()
    
