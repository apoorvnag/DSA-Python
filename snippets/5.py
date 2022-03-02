count = 1


def do_this():
    global count
    for i in (1, 2, 3):
        count += 1


do_this()
print(count)

"""
a. 4
b. 3
c. 2
d. 0

Ans. a
"""








