col = input("choose color: ")


class Colorizer:
    def __init__(self, collor):
        # self._text = text
        self._collor = collor

    def __enter__(self):
        collordict = {
            "grey": "\033[90m",
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "pink": "\033[95m",
            "turquoise": "\033[96m",
        }
        if self._collor not in collordict:
            return print("color does not exist")
        print(collordict[self._collor], end="")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("\033[0m", end="")


with Colorizer(col):
    print("printed in", col)
print("printed in default color")
