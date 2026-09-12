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
        assert sys.argv[2].lstrip("+-").isdigit(), (
            "the arguments are bad"
        )
        print(filterstring(sys.argv[1], int(sys.argv[2])))
    except AssertionError as error:
        print("AssertionError: ", error)


if __name__ == "__main__":
    main()
