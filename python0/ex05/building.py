import sys


def count_inside_fun(string, to_check):
    """count from to_check, how many letters there in string"""
    count = 0
    for char in string:
        if char in to_check:
            count += 1
    return count


def punctuation_marks(string):
    """this function is for the punctuation count"""
    return count_inside_fun(string, "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")


def string_details(string):
    """this function is to give you the details of the string"""
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    print(f"The text contains {len (string)} characters:")
    print(count_inside_fun(string, upper), "upper letters")
    print(count_inside_fun(string, lower), "lower letters")
    print(count_inside_fun(string, punctuation), "punctuation marks")
    print(count_inside_fun(string, " "), "spaces")
    print(count_inside_fun(string, "0123456789"), "digits")


def main():
    """this is the main function"""
    argc = len(sys.argv)
    if argc == 2:
        string_details(sys.argv[1])
    elif argc == 1:
        input_text = input("What is the text to count?\n")
        string_details(input_text)
    else:
        print("AssertionError")


if __name__ == "__main__":
    main()
