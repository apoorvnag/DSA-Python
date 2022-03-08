d1 = {
    1: 'apple',
    2: 'mango'
}

d2 = {
    2: 'banana',
    3: 'guava'
}

# print(d1)
# print(d2)

# d1.update(d2)

# print(d1)

# overwrites the values of the same key
# print({**d1, **d2})
# print({**d2, **d1})

# print(d1 | d2)

print({0} | {False})
print({False} | {0})


def say_hello(*, a, b, class_):
    print(a)
    print(b)
    print(class_)

say_hello(a=1,b=3, class_= 'asd')


