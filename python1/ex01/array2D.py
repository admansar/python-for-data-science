import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    slice_me(family: list, start: int, end: int) -> list
    this function takes a 2D array as a parameter print
    it shape and return truncated version of the given array
    from the start to the end
    """
    if type(family) is list and type(start) is start and type(end) is int:
        return None
    matrix = np.array(family)
    if np.all(matrix.shape[1:] == matrix.shape[:-1]):
        return None
    i, j = matrix.shape
    print(f"My shape is : ({i}, {j})")
    if start < 0:
        start = 0
    size = end - start
    if size <= 0:
        size = 1
    print(f"My new shape is : ({size}, {j})")
    vect = matrix.tolist()
    return vect[start:start + size]
