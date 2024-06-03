from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive: bool = True, family_name:
                 str = "Baratheon", eyes: str = "brown", hairs: str = "dark"):
        """init a Baratheon membre"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self) -> None:
        """ announce he died (the truth you killed him)"""
        if self.is_alive:
            self.is_alive = False

    def __str__(self) -> str:
        """print data for easy read for the user"""
        return f"Vector: ('{self.family_name}'\
                , '{self.eyes}', '{self.hairs}') "

    def __repr__(self) -> str:
        """print data for debugger"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name: str, is_alive: bool = True, family_name:
                 str = "Lannister", eyes: str = "blue", hairs: str = "light"):
        """init a Lannister membre"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self) -> None:
        """ announce he died (the truth you killed him)"""
        if self.is_alive:
            self.is_alive = False

    def __str__(self) -> str:
        """print data for debugger"""
        return f"Vector: ('{self.family_name}'\
                , '{self.eyes}', '{self.hairs}') "

    def __repr__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def create_lannister(first_name: str, is_alive: bool = True):
        return Lannister(first_name, is_alive)
