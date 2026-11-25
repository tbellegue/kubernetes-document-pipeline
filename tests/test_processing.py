from app.processing import (
    character_count,
    normalize_text,
    sentence_count,
    top_words,
    unique_word_count,
    word_count,
)


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


# word_count

def test_word_count_counts_repeated_words_and_ignores_punctuation():
    assert word_count("Hello, hello! -- world.") == 3


def test_word_count_empty_string():
    assert word_count("") == 0


# character_count

def test_character_count_counts_letters_spaces_and_punctuation():
    assert character_count("Hi, you!") == 8


def test_character_count_empty_string():
    assert character_count("") == 0


# sentence_count

def test_sentence_count_splits_on_all_terminators():
    assert sentence_count("Hello. How are you? Great!") == 3


def test_sentence_count_ignores_empty_pieces():
    assert sentence_count("Wait... what?!  ") == 2


def test_sentence_count_text_without_terminator_is_one_sentence():
    assert sentence_count("no punctuation here") == 1


def test_sentence_count_empty_and_punctuation_only():
    assert sentence_count("") == 0
    assert sentence_count(" ?!. ") == 0


# unique_word_count

def test_unique_word_count_ignores_case():
    assert unique_word_count("The the THE cat") == 2


def test_unique_word_count_ignores_punctuation():
    assert unique_word_count("Hello, hello! hello? World.") == 2


def test_unique_word_count_keeps_internal_apostrophes():
    assert unique_word_count("don't dont") == 2


def test_unique_word_count_empty_string():
    assert unique_word_count("") == 0


# top_words

def test_top_words_orders_by_frequency():
    text = "a b b c c c"
    assert top_words(text, 2) == [("c", 3), ("b", 2)]


def test_top_words_breaks_ties_alphabetically():
    text = "pear apple banana apple pear banana"
    assert top_words(text, 3) == [("apple", 2), ("banana", 2), ("pear", 2)]


def test_top_words_mixed_case_and_punctuation():
    text = "Dog! dog, DOG. Cat cat."
    assert top_words(text) == [("dog", 3), ("cat", 2)]


def test_top_words_fewer_words_than_n():
    assert top_words("one two", n=5) == [("one", 1), ("two", 1)]


def test_top_words_default_n_is_five():
    assert len(top_words("a b c d e f g")) == 5


def test_top_words_empty_string():
    assert top_words("") == []


def test_top_words_non_positive_n():
    assert top_words("a a b", n=0) == []
    assert top_words("a a b", n=-1) == []
