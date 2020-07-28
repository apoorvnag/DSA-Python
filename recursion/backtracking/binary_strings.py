def append_string(num, l):
    return [num + el for el in l]


def bin_strings(n):
    if n == 0:
        return []
    if n == 1:
        return ['0', '1']
    else:
        return append_string('0', bin_strings(n - 1) + append_string('1', bin_strings(n - 1)))


if __name__ == '__main__':
    print(bin_strings(2))
