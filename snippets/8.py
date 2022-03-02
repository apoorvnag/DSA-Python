class stud:
    'Base class for all students'

    def __init__(self, roll_no, grade):
        self.roll_no = roll_no
        self.grade = grade

    def display(self):
        print("Roll no : ", self.roll_no, ", Grade: ", self.grade)


print(stud.__doc__)


"""
a. Exception is thrown
b. __main__
c. Nothing is displayed
d. Base class for all students


Ans. d

Explanation : __doc__ that provides a documentation of the object.
"""