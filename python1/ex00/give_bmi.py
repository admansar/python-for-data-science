

def give_bmi(height, weight):
    """
    give_bmi(height: list[int | float], weight: list[int | float])
     -> list[int | float]
    this function calculate the bmi
    it takes as argument 2 list of float or int
    the first list represent the height and the second one the weight
    in case of error it returns None
    """
    re = []
    if len(height) is not len(weight):
        print("should have the same length")
        return None
    for h, w in zip(height, weight):
        if not (type(h) is float or type(h) is int):
            print("the height should be int of float")
            return None
        if not (type(w) is float or type(w) is int):
            print("the weight should be int of float")
            return None
        re.append(w / (h * h))
    return re


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit(bmi: list[int | float], limit: int) -> list[bool]
    this function do a test if the list of bmi given is over or under limits
    it return a bool list (True if above the limit)
    in case of error it returns None
    """
    re = []
    for item in bmi:
        if not (type(item) is float or type(item) is int):
            print("should have a list of int or float")
            return None
        if item > limit:
            re.append(True)
        else:
            re.append(False)
    return re
