class calculator:
    vector = []

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """ dot product for two vectors"""
        tmp = 0
        for i, j in zip(V1, V2):
            tmp += i * j
        print("Dot product is: ", tmp)

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """ add two vectors """
        vector = [float(i + j) for i, j in zip(V1, V2)]
        print("Add Vector is : ", vector)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """soustraire two vectors """
        vector = [float(i - j) for i, j in zip(V1, V2)]
        print("Sous Vector is: ", vector)
