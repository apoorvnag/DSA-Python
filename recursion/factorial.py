def factorial(n):
    """
    Calculate factorial
    :param n:
    :return:
    """

    # Base Case
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(1))
