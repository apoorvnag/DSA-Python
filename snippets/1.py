class Glove:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        return self.__color


class Minion:

    def __init__(self, glove):
        self.__glove = glove
        self.__color = "Yellow"

    def get_glove(self):
        return self.__glove


black_glove = Glove("Black")
red_glove = Glove("Red")
bob = Minion(black_glove)
black_glove.set_color(red_glove.get_color())
# what print(#line)


"""
What should be placed in the place of #line to get the color of bob Minion’s glove ?

a. bob.__glove.__color
b. red_glove.get_color()
c. bob.get_glove().get_color()
d. bob.get_glove().__color


Ans. c
Explanation : Option C is correct as bob is the object of Minion class
"""


