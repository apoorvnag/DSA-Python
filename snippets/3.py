s1 = {3, 4}
s2 = {1, 2}
s3 = set()

i = 0
j = 0

for i in s1:
    for j in s2:
        s3.add((i, j))
        i += 1
        j += 1

print(s3)

"""
a. {(3, 4), (1, 2)}
b. Error
c. {(3, 1), (4, 1), (4, 2), (5, 2)}
d. {(3, 1), (4, 2), (4, 1), (5, 2)}

Ans. c

Above code runs for
i = 3 j = 1
i = 4 j = 2
i = 4 j = 1
i = 5 j = 2
{(3, 1), (4, 1), (4, 2), (5, 2)}
"""