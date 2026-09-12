import sys


def odd(n: int) -> None:
    """Print whether a number is odd or even."""
    if n % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")


def main() -> None:
    """Validate the command-line arguments and call odd."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1:
            return
        try:
            number = int(sys.argv[1])
        except ValueError:
            assert False, "argument is not an integer"
        odd(number)
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
