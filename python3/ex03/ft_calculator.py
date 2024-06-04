class calculator:
    def __init__(self, vector: list):
        """ init calculator class """
        if isinstance(vector, list):
            self.vector = vector[:]
        else:
            raise Exception("calclutor class takes a list as a parametre")

    def check_len(self, v1: list, v2: list):
        """check if the len of two vector is equals or not
        if not it throw a exception
        """
        if len(v1) != len(v2):
            raise Exception("should have the same size to add them")

    def check_zero(self, object):
        """check if there is a zero in the int, float, list or even
        the calculator, in case it is, it throw a exception
        """
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
        """add the self object to any object of any type possible !!
        throw an Exception if its not possible
        """
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
        """multiply the self object to any object of any type possible !!
        throw an Exception if its not possible
        """
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
        """sub the self object to any object of any type possible !!
        throw an Exception if its not possible
        """
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
        """devide the self object to any object of any type possible !!
        throw an Exception if its not possible
        """
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
