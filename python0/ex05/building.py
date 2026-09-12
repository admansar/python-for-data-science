import sys


def count_characters(text: str, characters: str) -> int:
    """Return the number of characters in text that occur in characters."""
    return sum(
        char in characters
        for char in text
    )


def string_details(text: str) -> None:
    """Print counts of uppercase, lowercase, punctuation, spaces,
    and digits."""
    uppercase = sum(char.isupper() for char in text)
    lowercase = sum(char.islower() for char in text)
    punctuation = count_characters(
        text, "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    )
    spaces = sum(char.isspace() for char in text)
    digits = sum(char.isdigit() for char in text)
    print(f"The text contains {len(text)} characters:")
    print(uppercase, "upper letters")
    print(lowercase, "lower letters")
    print(punctuation, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")


def main():
    """Read text from an argument or standard input and print its details."""
    try:
        assert len(sys.argv) <= 2, "more than one argument"
        if len(sys.argv) == 2 and sys.argv[1]:
            string_details(sys.argv[1])
            return
        print("What is the text to count?")
        string_details(sys.stdin.read())
    except AssertionError:
        print("AssertionError")


if __name__ == "__main__":
    main()
