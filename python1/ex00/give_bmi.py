import numpy

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    re = []
    print(type(height[0]) == float)
    if len(height) is not len(weight):
        print("should have the same lentgh")
        return  None
    for h, w in zip(height, weight):
        re.append(w / (h * h))
    return re

list_h = [1.78, 1]
list_w = [88]

print (give_bmi(list_h, list_w))
