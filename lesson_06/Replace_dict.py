from functools import wraps


def mask_data(target_key: str, replace_with: str = "*"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            kwargs[target_key] = replace_with

            return func(*args, **kwargs)

        return wrapper

    return decorator


# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# TEST OUTPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")


"""example 2 """


def mask_data(target_key: str, replace_with: str = "*"):
    def decorator(func):
        """without @wraps(func) works the same way."""

        def wrapper(*args, **kwargs):
            kwargs[target_key] = replace_with

            return func(*args, **kwargs)

        return wrapper

    return decorator


# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# TEST OUTPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
