from functools import wraps


def big_o(time_complexity: str, space_complexity: str = ""):
    """Decorate a function to print its complexity."""

    def inner(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(
                f"{f.__mod__}:{f.__name__} Has BigO({time_complexity=}, {space_complexity=})"
            )
            return f(*args, **kwargs)

        return wrapper

    return inner
