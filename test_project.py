import pytest
import os
from project import load_riddles, update_leaderboard, save_history

# --- Test load_riddles ---
def test_load_riddles_easy():
    riddles = load_riddles("easy")
    assert isinstance(riddles, list)
    assert all(isinstance(r, tuple) and len(r) == 2 for r in riddles)
    assert len(riddles) > 0

def test_load_riddles_invalid():
    # Should return empty or exit if no riddles of that difficulty
    import sys
    import builtins

    # Temporarily override sys.exit to catch exit call
    original_exit = sys.exit
    sys.exit = lambda *args: None
    try:
        load_riddles("nonexistentdifficulty")
    finally:
        sys.exit = original_exit

# --- Test update_leaderboard ---
def test_update_leaderboard_creates_file(tmp_path):
    leaderboard_file = tmp_path / "leaderboard.txt"
    os.chdir(tmp_path)
    
    update_leaderboard("Alice", 5)
    
    assert leaderboard_file.exists()
    with open(leaderboard_file, "r") as f:
        lines = f.readlines()
    assert any("Alice|5" in line for line in lines)

def test_update_leaderboard_sorting(tmp_path):
    leaderboard_file = tmp_path / "leaderboard.txt"
    os.chdir(tmp_path)
    
    # Add multiple entries
    update_leaderboard("Bob", 2)
    update_leaderboard("Carol", 7)
    
    with open(leaderboard_file, "r") as f:
        lines = f.readlines()
    
    # Highest score should be first
    scores = [int(line.strip().split("|")[1]) for line in lines]
    assert scores == sorted(scores, reverse=True)

# --- Test save_history ---
def test_save_history_creates_file(tmp_path):
    history_file = tmp_path / "history.txt"
    os.chdir(tmp_path)
    
    save_history("Dave", "medium", 3)
    
    assert history_file.exists()
    with open(history_file, "r") as f:
        lines = f.readlines()
    assert any("Dave|medium|3" in line for line in lines)
