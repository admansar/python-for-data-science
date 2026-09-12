import sys


def filterstring(text: str, minimum_length: int) -> list[str]:
    """Return words longer than minimum_length from text."""
    return [
        word
        for word in text.split(" ")
        if word and (lambda value: len(value) > minimum_length)(word)
    ]


def main() -> None:
    """Validate the command-line arguments and print the filtered words."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        try:
            minimum_length = int(sys.argv[2])
        except ValueError:
            assert False, "the arguments are bad"
        print(filterstring(sys.argv[1], minimum_length))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
