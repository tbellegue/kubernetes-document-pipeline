from app.processing import normalize_text


def test_normalize_text_trims_edges():
    assert normalize_text("   hello world   ") == "hello world"


def test_normalize_text_collapses_multiple_spaces():
    assert normalize_text("hello    world") == "hello world"


def test_normalize_text_handles_tabs_and_newlines():
    assert normalize_text("hello\t\tworld\n\nagain") == "hello world again"


def test_normalize_text_empty_string():
    assert normalize_text("") == ""


def test_normalize_text_whitespace_only():
    assert normalize_text("   \n\t   ") == ""
