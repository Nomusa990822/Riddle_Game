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
        st.dataframe(df, use_container_width=True, hide_index=True)
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

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Games", len(df))
    col2.metric("Average Score", round(df["Score"].mean(), 2))
    col3.metric("Best Score", int(df["Score"].max()))

    st.bar_chart(df["Score"])


def get_points(difficulty):
    if difficulty == "easy":
        return 2
    if difficulty == "medium":
        return 3
    return 5


def reset_game():
    st.session_state.game_started = False
    st.session_state.score = 0
    st.session_state.question_number = 0
    st.session_state.questions = []
    st.session_state.question_start_time = None
    st.session_state.round_saved = False
    st.session_state.answer_submitted = False
    st.session_state.feedback = ""
    st.session_state.feedback_type = ""
    st.session_state.correct_answer = ""
    st.session_state.user_answer = ""


st.set_page_config(
    page_title="Riddle Quiz Game",
    page_icon="🧩",
    layout="centered"
)

# ---------------------------
# STYLING
# ---------------------------
st.markdown(
    """
    <style>
    .score-card {
        border: 1px solid #444;
        border-radius: 16px;
        padding: 18px;
        background: linear-gradient(135deg, #1f2937, #111827);
        margin-bottom: 16px;
        text-align: center;
    }
    .score-title {
        font-size: 15px;
        color: #9ca3af;
        margin-bottom: 6px;
    }
    .score-value {
        font-size: 34px;
        font-weight: bold;
        color: #fbbf24;
    }
    .review-card {
        border: 1px solid #444;
        border-radius: 14px;
        padding: 16px;
        margin-top: 10px;
        background-color: #161b22;
    }
    .review-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# SIDEBAR
# ---------------------------
with st.sidebar:
    st.header("🧩 Game Info")
    st.write("**Riddles per round:** 10")
    st.write("**Time per question:** 30 seconds")
    st.write("**Scoring system:**")
    st.write("- Easy = 2 points")
    st.write("- Medium = 3 points")
    st.write("- Hard = 5 points")
    st.markdown("---")
    st.write("Built by **Nomusa**")
    st.write("Powered by **Streamlit** 🚀")

# ---------------------------
# SESSION STATE
# ---------------------------
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_number" not in st.session_state:
    st.session_state.question_number = 0
if "questions" not in st.session_state:
    st.session_state.questions = []
if "question_start_time" not in st.session_state:
    st.session_state.question_start_time = None
if "round_saved" not in st.session_state:
    st.session_state.round_saved = False
if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "feedback_type" not in st.session_state:
    st.session_state.feedback_type = ""
if "correct_answer" not in st.session_state:
    st.session_state.correct_answer = ""
if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""

# ---------------------------
# HEADER
# ---------------------------
st.title("🧩 Riddle Quiz Game")
st.write("Test your brain with randomized riddles, timed challenges, and competitive scoring.")

name = st.text_input("Enter your name", value="")
difficulty = st.selectbox("Choose difficulty", ["easy", "medium", "hard"])
points_per_correct = get_points(difficulty)

# ---------------------------
# TOP CONTROLS
# ---------------------------
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
                st.session_state.answer_submitted = False
                st.session_state.feedback = ""
                st.session_state.feedback_type = ""
                st.session_state.correct_answer = ""
                st.session_state.user_answer = ""
                st.rerun()

with col2:
    if st.button("Reset", use_container_width=True):
        reset_game()
        st.rerun()

# ---------------------------
# MAIN GAME
# ---------------------------
if st.session_state.game_started:
    question_index = st.session_state.question_number
    progress = question_index / QUESTIONS_PER_ROUND

    st.progress(progress)

    st.markdown(
        f"""
        <div class="score-card">
            <div class="score-title">Current Score</div>
            <div class="score-value">{st.session_state.score} pts</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(f"{difficulty.title()} mode • {points_per_correct} points per correct answer")

    if question_index < QUESTIONS_PER_ROUND:
        riddle, answer = st.session_state.questions[question_index]

        if not st.session_state.answer_submitted:
            st_autorefresh(interval=1000, key="riddle_timer")

        if st.session_state.question_start_time is None:
            st.session_state.question_start_time = time.time()

        elapsed = int(time.time() - st.session_state.question_start_time)
        remaining = max(0, TIME_LIMIT - elapsed)

        st.subheader(f"Riddle {question_index + 1} of {QUESTIONS_PER_ROUND}")
        st.write(riddle)

        if st.session_state.answer_submitted:
            if st.session_state.feedback_type == "success":
                st.success(st.session_state.feedback)
            elif st.session_state.feedback_type == "error":
                st.error(st.session_state.feedback)

            st.markdown(
                f"""
                <div class="review-card">
                    <div class="review-title">📝 Answer Review</div>
                    <p><b>Your answer:</b> {st.session_state.user_answer}</p>
                    <p><b>Correct answer:</b> {st.session_state.correct_answer}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button("Next Question", key=f"next_{question_index}", use_container_width=True):
                st.session_state.question_number += 1
                st.session_state.question_start_time = time.time()
                st.session_state.answer_submitted = False
                st.session_state.feedback = ""
                st.session_state.feedback_type = ""
                st.session_state.correct_answer = ""
                st.session_state.user_answer = ""
                st.rerun()

        else:
            st.info(f"⏳ Time remaining: {remaining} seconds")

            user_answer = st.text_input("Your answer", key=f"answer_input_{question_index}")

            if remaining == 0:
                st.session_state.answer_submitted = True
                st.session_state.feedback = "⏱ Time's up!"
                st.session_state.feedback_type = "error"
                st.session_state.correct_answer = answer
                st.session_state.user_answer = "No answer submitted"
                st.rerun()

            if st.button("Submit Answer", key=f"submit_{question_index}", use_container_width=True):
                cleaned_user_answer = user_answer.strip()
                st.session_state.user_answer = cleaned_user_answer if cleaned_user_answer else "No answer submitted"

                if cleaned_user_answer.lower() == answer.lower():
                    st.session_state.score += points_per_correct
                    st.session_state.feedback = f"✅ Correct! +{points_per_correct} points"
                    st.session_state.feedback_type = "success"
                else:
                    st.session_state.feedback = "❌ Wrong!"
                    st.session_state.feedback_type = "error"

                st.session_state.correct_answer = answer
                st.session_state.answer_submitted = True
                st.rerun()

    else:
        st.success(f"🏆 Final Score: {st.session_state.score} points")

        if not st.session_state.round_saved:
            save_score(name.strip(), st.session_state.score)
            save_history(name.strip(), difficulty, st.session_state.score)
            st.session_state.round_saved = True

        show_leaderboard()
        show_player_stats(name.strip())

        if st.button("Play Again", use_container_width=True):
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
    <div style='text-align: center; font-size: 14px; color: gray;'>
        🧩 <b>Riddle Qiuz Game</b><br>
        Built by <b>Nomusa</b> | 2026<br>
        Powered by Streamlit 🚀
    </div>
    """,
    unsafe_allow_html=True
)
