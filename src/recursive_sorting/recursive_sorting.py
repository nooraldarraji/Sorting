# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # TO-DO

    la, ra = arrA[:], arrB[:]
    merged_arr = []

    while len(la) > 0 and len(ra) > 0:
        if la[0] < ra[0]:
            merged_arr.append(la.pop(0))
        else:
            merged_arr.append(ra.pop(0))

    return merged_arr + la + ra


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2:
        return arr

    m = len(arr) // 2

    sorted_left = merge_sort(arr[:m])
    sorted_right = merge_sort(arr[m:])

    return merge(sorted_left, sorted_right)


print(merge_sort([4, 3, 6, 9, 1, 8]))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
