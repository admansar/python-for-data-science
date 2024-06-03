from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        defaut constructeur for the abstract Character
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        pass


class Stark(Character):
    """
    ---
    a Character subclass that have a first_name and a is_alive status
    functions:
        die(self) -> None : set the alive status to false
    ---
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
     ---
     default const for the Stark class, sub-class of Character class
     have two args :
     first_name : the name
     is_alive : life stat (set to True by default)
     ---
        """
        super().__init__(first_name)

    def die(self) -> None:
        """
     ---
     die(None) -> None:
     this function set the is_alive status to False.
     ---
     """
        if self.is_alive:
            self.is_alive = False
