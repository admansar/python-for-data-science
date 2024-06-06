import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """creat a random id for about 15 letters"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """creat a student, takes name and surname \
            and gives him a unique login and id"""
    name: str
    surname: str
    active: bool = True
    id: str = field(init=False)
    login: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[:1] + self.surname[:]
        self.id = generate_id()
    # post_init is called after init in dataclasses
