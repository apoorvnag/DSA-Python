def swap(arr, pivot, ub):
    arr[pivot], arr[ub] = arr[ub], arr[pivot]


def partition(arr, low, high):
    pivot = low
    swap(arr, pivot, high)

    for i in range(low, high):
        if arr[i] < arr[high]:
            swap(arr, i, low)
            low += 1

    swap(arr, low, high)

    return low


def quick_sort(arr, lb, ub):
    if lb < ub:
        pivot = partition(arr, lb, ub)
        quick_sort(arr, 0, pivot)
        quick_sort(arr, pivot + 1, ub)


if __name__ == '__main__':
    arr = [10, 50, 60, 40, 30, 20, 70, 90, 80, 0, 1]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
