from project import check_answer


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
