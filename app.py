import random
import time
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

RIDDLE_FILE = "riddles.txt"
LEADERBOARD_FILE = "leaderboard.txt"
HISTORY_FILE = "history.txt"
QUESTIONS_PER_ROUND = 10
TIME_LIMIT = 30


def load_riddles(level):
    riddles = []

    try:
        with open(RIDDLE_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) != 3:
                    continue

                difficulty, riddle, answer = parts
                if difficulty.strip().lower() == level.lower():
                    riddles.append((riddle.strip(), answer.strip().lower()))
    except FileNotFoundError:
        st.error("riddles.txt not found.")

    return riddles


def save_score(name, score):
    with open(LEADERBOARD_FILE, "a", encoding="utf-8") as file:
        file.write(f"{name},{score}\n")


def save_history(name, difficulty, score):
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"{name},{difficulty},{score}\n")


def get_leaderboard():
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
        pass

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores


def show_leaderboard():
    st.subheader("🏆 Global Leaderboard")
    scores = get_leaderboard()

    if scores:
        df = pd.DataFrame(scores[:10], columns=["Player", "Score"])
        st.table(df)
    else:
        st.info("No leaderboard data yet.")


def show_player_stats(player_name):
    rows = []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue

                name, difficulty, score = parts
                if name == player_name:
                    try:
                        rows.append((difficulty, int(score)))
                    except ValueError:
                        continue
    except FileNotFoundError:
        pass

    st.subheader("📊 Your Statistics")

    if not rows:
        st.info("No stats yet.")
        return

    df = pd.DataFrame(rows, columns=["Difficulty", "Score"])
    st.write("Total Games:", len(df))
    st.write("Average Score:", round(df["Score"].mean(), 2))
    st.write("Best Score:", int(df["Score"].max()))
    st.bar_chart(df["Score"])


def reset_game():
    st.session_state.game_started = False
    st.session_state.score = 0
    st.session_state.question_number = 0
    st.session_state.questions = []
    st.session_state.current_answer = ""
    st.session_state.question_start_time = None
    st.session_state.round_saved = False


st.set_page_config(page_title="Riddle Quiz Game", page_icon="🧩", layout="centered")

st.title("🧩 Riddle Quiz Game")
st.write("Play in your browser with 10 riddles per round and 30 seconds per question.")

if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_number" not in st.session_state:
    st.session_state.question_number = 0
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current_answer" not in st.session_state:
    st.session_state.current_answer = ""
if "question_start_time" not in st.session_state:
    st.session_state.question_start_time = None
if "round_saved" not in st.session_state:
    st.session_state.round_saved = False

name = st.text_input("Enter your name", value="")
difficulty = st.selectbox("Choose difficulty", ["easy", "medium", "hard"])

col1, col2 = st.columns(2)

with col1:
    if st.button("Start Game", use_container_width=True):
        if not name.strip():
            st.error("Please enter your name.")
        else:
            riddles = load_riddles(difficulty)

            if len(riddles) < QUESTIONS_PER_ROUND:
                st.error(f"Not enough riddles for {difficulty}. Need at least {QUESTIONS_PER_ROUND}.")
            else:
                st.session_state.questions = random.sample(riddles, QUESTIONS_PER_ROUND)
                st.session_state.score = 0
                st.session_state.question_number = 0
                st.session_state.game_started = True
                st.session_state.round_saved = False
                st.session_state.question_start_time = time.time()
                st.rerun()

with col2:
    if st.button("Reset", use_container_width=True):
        reset_game()
        st.rerun()

if st.session_state.game_started:
    st_autorefresh(interval=1000, key="riddle_timer")

    question_index = st.session_state.question_number
    progress = question_index / QUESTIONS_PER_ROUND
    st.progress(progress)

    if question_index < QUESTIONS_PER_ROUND:
        riddle, answer = st.session_state.questions[question_index]

        if st.session_state.question_start_time is None:
            st.session_state.question_start_time = time.time()

        elapsed = int(time.time() - st.session_state.question_start_time)
        remaining = max(0, TIME_LIMIT - elapsed)

        st.subheader(f"Riddle {question_index + 1} of {QUESTIONS_PER_ROUND}")
        st.write(riddle)
        st.info(f"⏳ Time remaining: {remaining} seconds")

        if remaining == 0:
            st.error(f"⏱ Time's up! Correct answer: {answer}")

            if st.button("Next Question", key=f"next_timeout_{question_index}"):
                st.session_state.question_number += 1
                st.session_state.question_start_time = time.time()
                st.rerun()
        else:
            user_answer = st.text_input(
                "Your answer",
                key=f"answer_input_{question_index}"
            )

            if st.button("Submit Answer", key=f"submit_{question_index}"):
                if user_answer.strip().lower() == answer.lower():
                    st.success("✅ Correct!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Wrong! Correct answer: {answer}")

                st.session_state.question_number += 1
                st.session_state.question_start_time = time.time()
                st.rerun()

        st.write(f"Current Score: {st.session_state.score}")
    else:
        st.success(f"🏆 Final Score: {st.session_state.score}/{QUESTIONS_PER_ROUND}")

        if not st.session_state.round_saved:
            save_score(name.strip(), st.session_state.score)
            save_history(name.strip(), difficulty, st.session_state.score)
            st.session_state.round_saved = True

        show_leaderboard()
        show_player_stats(name.strip())

        if st.button("Play Again"):
            reset_game()
            st.rerun()
else:
    show_leaderboard()

# ---------------------------
# FOOTER
# ---------------------------

st.markdown("---")

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117;
        color: gray;
        text-align: center;
        padding: 10px;
        font-size: 13px;
    }
    </style>

    <div class="footer">
        🧩 Riddle Quiz Game | Built by Nomusa | 2026 🚀
    </div>
    """,
    unsafe_allow_html=True
)
