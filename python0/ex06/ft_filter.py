def is_odd(n) -> bool:
    """is_odd(number) --> True or false
Return True if the number is odd else it return false"""
    if n % 2 == 1:
        return True
    return False


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        yield [item for item in iterable]
    yield [item for item in iterable if function(item)]


def main():
    tmp = [1, 2, 3, 4]
    it = ft_filter(is_odd, tmp)
    for num in it:
        print(num)


if __name__ == "__main__":
    main()
