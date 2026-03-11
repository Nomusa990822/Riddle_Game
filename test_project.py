from project import check_answer


def test_check_answer_correct():
    assert check_answer("piano", "piano") == True


def test_check_answer_case_insensitive():
    assert check_answer("Piano".lower(), "piano") == True


def test_check_answer_wrong():
    assert check_answer("door", "piano") == False


def test_check_answer_extra_spaces():
    assert check_answer("piano".strip(), "piano") == True


def test_check_answer_completely_different():
    assert check_answer("car", "piano") == False
