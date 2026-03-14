from project import load_riddles


def test_load_riddles():

    riddles = load_riddles()

    assert "easy" in riddles
    assert "medium" in riddles
    assert "hard" in riddles

    assert isinstance(riddles["easy"], list)
