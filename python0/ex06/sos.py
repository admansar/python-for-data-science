import sys


def sos(text: str) -> None:
    """Print the Morse Code representation of an alphanumeric string."""
    morse_code = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....", "6": "-....",
        "7": "--...", "8": "---..", "9": "----.", " ": "/",
    }
    assert isinstance(text, str), "the arguments are bad"
    encoded = []
    for character in text:
        code = morse_code.get(character.upper() if character != " " else " ")
        assert code is not None, "the arguments are bad"
        encoded.append(code)
    print(" ".join(encoded))


def main() -> None:
    """Validate the command-line arguments and encode the supplied text."""
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        sos(sys.argv[1])
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
