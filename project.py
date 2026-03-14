import random
import time
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

init(autoreset=True)

POINTS = {"easy": 1, "medium": 2, "hard": 3}
RIDDLE_FILE = "riddles.txt"
LEADERBOARD_FILE = "leaderboard.txt"
HISTORY_FILE = "history.txt"
STATS_FILE = "stats.txt"


def main():
    show_banner()
    player = input("Enter your name: ").strip()

    while True:
        mode = input("\nPlay 'game' or 'simulate'? ").strip().lower()
        if mode == "game":
            play_game_mode(player)
        elif mode == "simulate":
            results = run_simulation(1000)
            plot_simulation(results)
        else:
            print("Invalid option.")

        again = input("\nExit or continue? (exit/continue): ").strip().lower()
        if again == "exit":
            print("Goodbye!")
            break


def show_banner():
    print(Fore.CYAN + """
██████╗ ██╗██████╗ ██████╗ ██╗     ███████╗
██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝
██████╔╝██║██║  ██║██║  ██║██║     █████╗
██╔══██╗██║██║  ██║██║  ██║██║     ██╔══╝
██║  ██║██║██████╔╝██████╔╝███████╗███████╗
╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚══════╝
        RIDDLE QUIZ GAME
""")


def get_riddles(difficulty):
    riddles = []
    with open(RIDDLE_FILE, "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) != 3:
                continue
            diff, riddle, answer = parts
            if diff.lower() == difficulty:
                riddles.append((riddle, answer))
    return riddles


def play_game_mode(player):
    difficulty = input("Choose difficulty (easy/medium/hard): ").strip().lower()
    all_riddles = get_riddles(difficulty)
    if len(all_riddles) < 5:
        print("Not enough riddles found!")
        return

    selected = random.sample(all_riddles, 5)
    score = 0

    for riddle, answer in selected:
        print(Fore.BLUE + "\n" + riddle)
        start = time.time()
        user = input("Your answer: ").strip().lower()
        end = time.time()

        if end - start > 10:
            print(Fore.RED + "Time's up!")
            print("Answer was:", answer)
        else:
            if user == answer.lower():
                print(Fore.GREEN + "Correct!")
                score += POINTS[difficulty]
            else:
                print(Fore.RED + "Wrong! Answer:", answer)

    print(Fore.YELLOW + f"\nFinal score: {score}")
    update_leaderboard(player, score)
    update_history(player, difficulty, score)
    update_stats(player, score)
    show_leaderboard()
    show_player_stats(player)
    show_achievements(score)


def update_leaderboard(player, score):
    board = []
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            for line in f:
                name, sc = line.strip().split(",")
                board.append((name, int(sc)))
    except FileNotFoundError:
        pass

    board.append((player, score))
    board.sort(key=lambda x: x[1], reverse=True)
    board = board[:10]
    with open(LEADERBOARD_FILE, "w") as f:
        for name, sc in board:
            f.write(f"{name},{sc}\n")


def show_leaderboard():
    print(Fore.MAGENTA + "\n🏆 Leaderboard")
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            for idx, line in enumerate(f, 1):
                name, sc = line.strip().split(",")
                print(f"{idx}. {name} — {sc}")
    except FileNotFoundError:
        print("No leaderboard yet.")


def update_history(player, diff, score):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{player},{diff},{score}\n")


def update_stats(player, score):
    stats = {}
    try:
        with open(STATS_FILE, "r") as f:
            for line in f:
                name, games, total, best = line.strip().split(",")
                stats[name] = [int(games), int(total), int(best)]
    except FileNotFoundError:
        pass

    if player in stats:
        stats[player][0] += 1
        stats[player][1] += score
        stats[player][2] = max(stats[player][2], score)
    else:
        stats[player] = [1, score, score]

    with open(STATS_FILE, "w") as f:
        for nm, data in stats.items():
            f.write(f"{nm},{data[0]},{data[1]},{data[2]}\n")


def show_player_stats(player):
    try:
        with open(STATS_FILE, "r") as f:
            for line in f:
                name, games, total, best = line.strip().split(",")
                if name == player:
                    avg = int(total) / int(games)
                    print(Fore.CYAN + "\n📊 Your Stats:")
                    print(f"Games played: {games}")
                    print(f"Best score: {best}")
                    print(f"Average score: {avg:.1f}")
    except FileNotFoundError:
        pass


def show_achievements(score):
    ach = []
    if score >= 3:
        ach.append("🧠 Clever Thinker")
    if score >= 6:
        ach.append("🧩 Puzzle Solver")
    if score >= 9:
        ach.append("👑 Riddle King")
    if ach:
        print(Fore.YELLOW + "\n⭐ Achievements unlocked:")
        for a in ach:
            print("-", a)


def simulate_player(difficulty):
    total = 0
    for _ in range(5):
        chance = random.random()
        if difficulty == "easy":
            correct = chance < 0.9
        elif difficulty == "medium":
            correct = chance < 0.7
        else:
            correct = chance < 0.5
        if correct:
            total += POINTS[difficulty]
    return total


def run_simulation(n):
    results = {"easy": [], "medium": [], "hard": []}
    for _ in range(n):
        for d in results:
            results[d].append(simulate_player(d))
    return results


def plot_simulation(results):
    plt.figure(figsize=(8, 6))
    for d, scores in results.items():
        plt.hist(scores, bins=range(0, 16), alpha=0.5, label=d.capitalize())
    plt.title("Simulation of Player Scores by Difficulty")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
