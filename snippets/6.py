"""
Name mangling in Python


"""
class student:
    def __init__(self):
        self.marks = 97
        self.__cgpa = 8.7

    def display(self):
        print(self.marks)


obj = student()
print(obj._student__cgpa)



"""
a. The program runs fine and 8.7 is printed
b. Error because private class members can’t be accessed
c. Error because the proper syntax for name mangling hasn’t been implemented
d. The program runs fine but nothing is printed

Ans. a
No issues with the code. It will work fine.

No issues with the code. It will work fine.
In name mangling process any identifier with 
two leading underscore and one trailing underscore 
is textually replaced with _classname__identifier 
where classname is the name of the current class.

"""
