from typing import Any


def all_thing_is_obj(object: Any) -> int:
    """Print the required description for the object's type and return 42."""
    object_type = type(object)
    type_name = object_type.__name__.capitalize()
    if type_name == "Str":
        print(f"{object} is in the kitchen : {object_type}")
    elif type_name in ("List", "Tuple", "Set", "Dict"):
        print(f"{type_name} : {object_type}")
    else:
        print("Type not found")
    return 42
