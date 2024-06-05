def square(x: int | float) -> int | float:
    """takes x as a int or float and return the square"""
    if isinstance(x, (int, float)):
        return x ** 2
    else:
        raise Exception(f"could not calculate the square of {type(x)}")


def pow(x: int | float) -> int | float:
    """takes x as a int or float and returning it by the power of it self"""
    if isinstance(x, (int, float)):
        return x ** x
    else:
        raise Exception(f"could not calculate the power of {type(x)}")


def outer(x: int | float, function) -> object:
    """takes a int or float x as a parametre and aplicate the \
            function passed in the parametre to it """
    count = 0

    def inner() -> float:
        nonlocal count
        count += 1
        re = x
        for _ in range(count):
            re = function(re)
        return re
    return inner
# the outer calls the inner, so we keep calling the inner all the time
