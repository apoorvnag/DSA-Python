def toh(disks, start=1, end=3):
    if disks:
        toh(disks - 1, 1, 2)
        print('move disk {} from tower {} to tower {}'.format(disks, start, end))
        toh(disks - 1, 2, 3)


if __name__ == '__main__':
    toh(3, 1, 3)
