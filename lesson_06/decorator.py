from functools import wraps


def reverse_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if type(func()) is str:
            return func(*args, **kwargs)[::-1]
        else:
            return None

    return wrapper


@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year() -> int:
    return 1957


print(get_university_name(), get_university_founding_year(), sep="\n")

# example 2

# def reverse_string(func):
#     def wrapper():
#         if type(func()) is str:
#             return func()[::-1]
#         else:
#             return None
#     return wrapper
#
#
# @reverse_string
# def get_university_name() -> str:
#     return "Western Institute of Technology and Higher Education"
#
#
# @reverse_string
# def get_university_founding_year() -> int:
#     return 1957
#
#
# print(
#     get_university_name(),
#     get_university_founding_year(),
#     get_university_name(),
#     get_university_founding_year(),
#     sep="\n"
# )
