from abc import ABC, abstractclassmethod
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(cls):
        pass


class Rectangle(Shape):
    def draw(self):
        print("----\n|  |\n----")


class Circle(Shape):
    def draw(self):
        print(" --\n-  -\n --")


def get_shape() -> Shape:
    rectangle = Rectangle()
    circle = Circle()
    """
    This function should return any instance of a Shape class
    In our example it is Rectangle or Circle
    """
    options: list[Shape] = [rectangle, circle]
    return choice(options)


def main():

    """
    In Rectangle is used I'd like to see:

    ----
    |  |
    ----

    If Circle is used:
      --
     -  -
      --
    """
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
