def remove_spaces(text: str) -> str:
    return text.replace(" ", "")


def test_remove_empty_string():
    assert remove_spaces("") == ""


def test_remove_spaces_only_spaces():
    assert remove_spaces("     ") == ""


def test_remove_spaces_tabs():
    assert remove_spaces("hello\t world") == "hello\tworld"
