from project import check_answer, get_points


def test_check_answer_exact_match():
    assert check_answer("piano", "piano") is True


def test_check_answer_case_insensitive():
    assert check_answer("PiaNo", "piano") is True


def test_check_answer_strips_spaces():
    assert check_answer("  piano  ", "piano") is True


def test_check_answer_wrong():
    assert check_answer("keyboard", "piano") is False


def test_check_answer_empty():
    assert check_answer("", "piano") is False


def test_get_points_easy():
    assert get_points("easy") == 2


def test_get_points_medium():
    assert get_points("medium") == 3


def test_get_points_hard():
    assert get_points("hard") == 5
