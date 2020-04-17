def fibo(n):
    if n == 0:
        return 0


if __name__ == '__main__':
    r = int(input('Enter the range\n'))

    a = 1
    b = 1

    if r < 1:
        print('Enter a positive number')
        exit(0)
    if r == 1:
        print(a)
        exit(0)
    count = 1
    while count <= r:
        print(b)
        temp = b
        b = a + b
        a = temp
        count = count + 1
