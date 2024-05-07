import sys


def sos(string):
    """sos(string) --> this function turns the alphanum to morce code"""
    morse_code_dict = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..", " ": "/ ", "a": ".-", "b": "-...", "c": "-.-.",
        "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
        "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
        "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
        "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-",
        "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
        "0": "------", "1": ".-----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----."}
    fill = ""
    for char in string:
        the_char = morse_code_dict.get(char)
        if the_char is None:
            raise AssertionError("AssertionError: the arguments are bad")
        fill += the_char + " "
    print(fill[:len(fill)-1])


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")
        sos(sys.argv[1])
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
