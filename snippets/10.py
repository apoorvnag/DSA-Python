class Parent:
    def __init__(self):
        self.x = 0


class ChildClass(Parent):
    def __init__(self):
        self.y = 1


def main():
    b = ChildClass()
    print(b.x, b.y)


main()


"""
a. 0 1
b. 0 0
c. Error
d. 1 0


Ans. c

Explanation : ‘Derived_Test’ object has no attribute ‘x’
"""
