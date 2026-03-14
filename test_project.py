import pytest
from project import load_riddles


def test_load_riddles_returns_dictionary():
    """
    Test that load_riddles() returns a dictionary.
    """

    riddles = load_riddles()

    assert isinstance(riddles, dict)


def test_riddle_categories_exist():
    """
    Test that the expected difficulty levels exist.
    """

    riddles = load_riddles()

    assert "easy" in riddles
    assert "medium" in riddles
    assert "hard" in riddles


def test_riddles_are_lists():
    """
    Test that each difficulty category contains a list.
    """

    riddles = load_riddles()

    assert isinstance(riddles["easy"], list)
    assert isinstance(riddles["medium"], list)
    assert isinstance(riddles["hard"], list)


def test_riddles_have_question_and_answer():
    """
    Test that each riddle has a question and answer tuple.
    """

    riddles = load_riddles()

    for difficulty in riddles:
        for riddle in riddles[difficulty]:
            assert isinstance(riddle, tuple)
            assert len(riddle) == 2
