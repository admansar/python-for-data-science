from typing import Any


def NULL_not_found(object: Any) -> int:
    """Print a label for a recognised null-like value and return its status."""
    object_type = type(object)
    if object_type is type(None):
        print(f"Nothing : {object} {object_type}")
    elif object_type is float:
        print(f"Cheese : {object} {object_type}")
    elif object_type is int:
        print(f"Zero : {object} {object_type}")
    elif object_type is str and len(object) == 0:
        print(f"Empty : {object_type}")
    elif object_type is bool:
        print(f"Fake : {object} {object_type}")
    else:
        print("Type not Found")
        return 1
    return 0
