

def give_bmi(height, weight):
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
