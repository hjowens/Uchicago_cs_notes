from games import WordGuessingGame
import pytest


def test_game_no_guesses() -> None:
    """
    Creates a game, and checks that all the properties
    at the start of the game contain valid values.
    """

    game = WordGuessingGame("abcde", 6)

    assert game.word == "abcde"
    assert game.masked_word == "-----"
    assert game.guesses_remaining == 6
    assert not game.done
    assert not game.guessed_all


def test_single_correct_guess() -> None:
    """
    Creates a game, guesses one letter correctly,
    and checks that all properties have correct values
    """

    game = WordGuessingGame("abcde", 6)
    game.guess("c")

    assert game.word == "abcde"
    assert game.masked_word == "--c--"
    assert game.guesses_remaining == 6
    assert not game.done
    assert not game.guessed_all


def test_single_correct_guess_multiple_occurrences() -> None:
    """
    Creates a game, guesses one letter correctly
    (the letter appears multiple times in the word),
    and checks that all properties have correct values
    """

    game = WordGuessingGame("aabbaaba", 6)
    game.guess("b")

    assert game.word == "aabbaaba"
    assert game.masked_word == "--bb--b-"
    assert game.guesses_remaining == 6
    assert not game.done
    assert not game.guessed_all


def test_single_incorrect_guess() -> None:
    """
    Creates a game, guesses one letter incorrectly,
    and checks that all properties have correct values
    """

    game = WordGuessingGame("abcde", 6)
    game.guess("z")

    assert game.word == "abcde"
    assert game.masked_word == "-----"
    assert game.guesses_remaining == 5
    assert not game.done
    assert not game.guessed_all


def test_game_win() -> None:
    """
    Creates a game, guess letters in a way that
    will result in a win, and verify that all
    properties return the expected values
    """

    game = WordGuessingGame("abcde", 6)
    game.guess("a")
    game.guess("x")
    game.guess("b")
    game.guess("y")
    game.guess("c")
    game.guess("z")
    game.guess("d")
    game.guess("e")

    assert game.word == "abcde"
    assert game.masked_word == "abcde"
    assert game.guesses_remaining == 3
    assert game.done
    assert game.guessed_all


def test_game_lose() -> None:
    """
    Creates a game, guess letters in a way that
    will result in a loss, and verify that all
    properties return the expected values
    """

    game = WordGuessingGame("abcde", 6)
    game.guess("a")
    game.guess("x")
    game.guess("b")
    game.guess("y")
    game.guess("c")
    game.guess("z")
    game.guess("m")
    game.guess("n")
    game.guess("o")

    assert game.word == "abcde"
    assert game.masked_word == "abc--"
    assert game.guesses_remaining == 0
    assert game.done
    assert not game.guessed_all


def test_valid_letter_length() -> None:
    """
    Checks that guess() raises an exception
    if given a string containing more than
    one letter
    """

    game = WordGuessingGame("abcde", 6)

    with pytest.raises(ValueError):
        game.guess("abc")

    assert game.word == "abcde"
    assert game.masked_word == "-----"
    assert game.guesses_remaining == 6
    assert not game.done
    assert not game.guessed_all


def test_valid_letter_alpha() -> None:
    """
    Checks that guess() raises an exception
    if given a string containing a character
    that is not a letter
    """

    game = WordGuessingGame("abcde", 6)

    with pytest.raises(ValueError):
        game.guess("7")

    assert game.word == "abcde"
    assert game.masked_word == "-----"
    assert game.guesses_remaining == 6
    assert not game.done
    assert not game.guessed_all


def test_valid_letter_uppercase() -> None:
    """
    Checks that guess() works correctly
    if given an uppercase letter
    """

    game = WordGuessingGame("abcde", 6)

    game.guess("C")

    assert game.word == "abcde"
    assert game.masked_word == "--c--"
    assert game.guesses_remaining == 6
    assert not game.done
    assert not game.guessed_all


def test_already_guessed() -> None:
    """
    Checks that guess() raises an exception
    if given a letter that has already been
    guessed
    """

    game = WordGuessingGame("abcde", 6)

    game.guess("c")

    with pytest.raises(ValueError):
        game.guess("c")

    assert game.word == "abcde"
    assert game.masked_word == "--c--"
    assert game.guesses_remaining == 6
    assert not game.done
    assert not game.guessed_all
