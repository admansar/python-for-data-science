from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """king class, the diamond trap example !!"""
    def set_eyes(self, eyes: str) -> None:
        """ set the eyes value"""
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        """ set the hairs value"""
        self.hairs = hairs

    def get_eyes(self) -> str:
        """get the eyes value"""
        return self.eyes

    def get_hairs(self) -> str:
        """get the hairs value"""
        return self.hairs
