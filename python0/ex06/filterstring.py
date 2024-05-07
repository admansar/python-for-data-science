import sys


def filterstring(array):
    """filterstring (array)
--> print from string the words that have more than a number;
it takes a array (usually the argv), it takes array [1]
split it by spaces and list it in a list, if there is a
element that have less then the number indicated in array[2]
it will not be printed """
    if len(array) != 3 or (not array[2].isdigit()):
        raise AssertionError("AssertionError: the arguments are bad")
    lst = [word for word in array[1].split(' ') if len(word) > int(array[2])]
    print(lst)


def main():
    try:
        filterstring(sys.argv)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
