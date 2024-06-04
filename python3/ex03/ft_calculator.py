class calculator:
    def __init__(self, vector: list):
        if isinstance(vector, list):
            self.vector = vector[:]
        else:
            raise Exception("calclutor class takes a list as a parametre")

    def check_len(self, v1: list, v2: list):
        if len(v1) != len(v2):
            raise Exception("should have the same size to add them")

    def check_zero(self, object):
        if isinstance(object, (int, float)):
            if object == 0:
                raise Exception("cant devide by 0")
        elif isinstance(object, list):
            if 0 in object:
                raise Exception("cant devide by 0")
        elif isinstance(object, calculator):
            if 0 in object.vector:
                raise Exception("cant devide by 0")

    def __add__(self, object) -> None:
        if isinstance(object, (int, float)):
            self.vector = [it + object for it in self.vector]
            print(self.vector)
        elif isinstance(object, list):
            self.check_len(object, self.vector)
            self.vector = [it1 + it2 for it1, it2 in zip(self.vector, object)]
            print(self.vector)

        elif isinstance(object, calculator):
            self.check_len(object.vector, self.vector)
            self.vector = [it + it2 for it, it2 in
                           zip(self.vector, object.vector)]
            print(self.vector)
        else:
            raise Exception("can't add a calculator with a " + type(object))

    def __mul__(self, object) -> None:
        if isinstance(object, (int, float)):
            self.vector = [i * object for i in self.vector]
            print(self.vector)
        elif isinstance(object, list):
            self.check_len(object, self.vector)
            self.vector = [i * j for i, j in zip(self.vector, object)]
            print(self.vector)
        elif isinstance(object, calculator):
            self.check_len(object.vector, self.vector)
            self.vector = [i * j for i, j in zip(self.vector, object.vector)]
            print(self.vector)
        else:
            raise Exception("can't do product of a calculator with a "
                            + type(object))

    def __sub__(self, object) -> None:
        if isinstance(object, (int, float)):
            self.vector = [i - object for i in self.vector]
            print(self.vector)
        elif isinstance(object, list):
            self.check_len(object, self.vector)
            self.vector = [i - j for i, j in zip(self.vector, object)]
            print(self.vector)
        elif isinstance(object, calculator):
            self.check_len(object.vector, self.vector)
            self.vector = [i - j for i, j in zip(self.vector, object.vector)]
            print(self.vector)
        else:
            raise Exception("can't do sub a calculator() with a "
                            + type(object))

    def __truediv__(self, object) -> None:
        try:
            self.check_zero(object)
            if isinstance(object, (int, float)):
                self.vector = [i / object for i in self.vector]
                print(self.vector)
            elif isinstance(object, list):
                self.check_len(object, self.vector)
                self.vector = [i / j for i, j in zip(self.vector, object)]
                print(self.vector)
            elif isinstance(object, calculator):
                self.check_len(object.vector, self.vector)
                self.vector = [i / j for i, j in zip(self.vector,
                               object.vector)]
                print(self.vector)
            else:
                raise Exception("can't divide a calculator() with a "
                                + type(object))
        except Exception as e:
            print(f"Error: {e}")
