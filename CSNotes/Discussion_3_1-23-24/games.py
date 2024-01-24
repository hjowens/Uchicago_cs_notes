"""
Module providing game-related classes.

So far, only one class is available:

- WordGuessingGame: Implements a word-guessing game

"""

import string


class WordGuessingGame:
    """
    Class for a word-guessing game. In this game,
    we start from a word that appears completely
    masked (the player only knows the number of
    letters in the word).

    The player can guess one letter at a time,
    and has a limit on the number of incorrect
    guesses they can make. If the player guesses
    a letter that is contained in the word, all
    instances of that letter are unmasked. Otherwise,
    the number of remaining guesses is decremented
    by one.

    The game ends when the player unmasks all the letters,
    or when they run out of guesses.

    Attributes:
        _word: The word that is being guessed
        _masked: A list of booleans indicating what letters
            are currently masked (e.g., if masked[2] is True,
            it means the third letter in the word has not been
            guessed correctly yet)
        _letters_guessed: The letters guessed so far by the
            player
        _guesses_remaining: The number of (incorrect) guesses
            remaining in the game.

    Example:
        >>> g = WordGuessingGame("python", 7)
        >>> g.masked_word
        '------'
        >>> g.guess("p")
        >>> g.masked_word
        'p-----'
        >>> g.guesses_remaining
        7
        >>> g.guess("a")
        >>> g.masked_word
        'p-----'
        >>> g.guesses_remaining
        6
        >>> g.done
        False
        >>> g.guess("y")
        >>> g.guess("t")
        >>> g.guess("h")
        >>> g.guess("o")
        >>> g.guess("n")
        >>> g.masked_word
        'python'
        >>> g.done
        True
        >>> g.guessed_all
        True
    """

    _word: str
    _masked: list[bool]
    _letters_guessed: set[str]
    _guesses_remaining: int

    def __init__(self, word: str, num_guesses: int):
        """
        Constructor

        Args:
            word: Word to guess
            num_guesses: Maximum number of incorrect guesses
        """
        self._word = word
        self._masked = [True for _ in range(len(word))]
        self._letters_guessed = set()
        self._guesses_remaining = num_guesses

    @property
    def word(self) -> str:
        """
        Returns: The word to guess
        """
        return self._word

    @property
    def masked_word(self) -> str:
        """
        Returns: The masked word. Any letter that has
            not been guessed correctly will be replaced with
            a hyphen.
        """
        mw = ""
        for letter, is_masked in zip(self._word, self._masked):
            if is_masked:
                mw += "-"
            else:
                mw += letter
        return mw

    @property
    def guesses_remaining(self) -> int:
        """
        Returns: The number of guesses remaining
        """
        return self._guesses_remaining

    @property
    def done(self) -> bool:
        """
        Returns: True if the game is done, False otherwise. The
            game is done if the player has guessed all the letters
            in the word, or if they run out of guesses.
        """
        if self._guesses_remaining == 0:
            return True

        if self.guessed_all:
            return True

        return False

    @property
    def guessed_all(self) -> bool:
        """
        Returns: True if the player has guessed all the letters
            in the word, False otherwise.
        """
        return not any(self._masked)

    def guess(self, letter: str) -> None:
        """
        Guess a letter in the word. If the letter
        appears in the word (and has not already been
        guessed) all occurrences of the letter are
        unmasked in the word. Otherwise, the number
        of remaining guesses is decremented by one.

        Args:
            letter: The letter to guess

        Raises:
            ValueError: If any of the following apply:
                - The letter parameter contains a string
                  with more than one letter.
                - The letter parameter does not contain
                  a letter between 'a' and 'z'
                - The letter has already been guessed

        Returns: None
        """

        # Validate the letter parameter
        if len(letter) > 1:
            raise ValueError(f"Your guess must be a single letter (got '{letter}')")

        letter = letter.lower()

        if letter not in string.ascii_letters:
            raise ValueError(f"Your guess must be a letter between 'a' and 'z' (got '{letter}')")

        if letter in self._letters_guessed:
            raise ValueError(f"Already guessed: {letter}")

        # At this point, we know we have a lowercase letter that hasn't
        # already been guessed.

        # Add the letter to the set of guessed letters
        self._letters_guessed.add(letter)

        # Unmask any occurrences of that letter
        unmasked = 0
        for i, l in enumerate(self._word):
            if l == letter:
                self._masked[i] = False
                unmasked += 1

        # If we didn't unmask any letters, decrement the
        # number of guesses
        if unmasked == 0:
            self._guesses_remaining -= 1
