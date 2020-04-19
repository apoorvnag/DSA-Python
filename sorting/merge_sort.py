def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        merge_sort(left_arr)
        right_arr = arr[mid:]
        merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i+ 1
            else:
                arr[k] = right_arr[j]
                j=j+1
            k=k+1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1





if __name__ == '__main__':
    arr = [10, 50, 60, 40, 30, 20, 70, 90, 80, 0, 1, 50, 30]
    merge_sort(arr)
    print(arr)