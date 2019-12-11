# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr) - 1):
        r = i + 1
        l = i
        while l >= 0:
            if arr[l] > arr[r]:
                arr[l], arr[r] = (arr[r], arr[l])
                l -= 1
                r -= 1
            else:
                break
    return arr


# print(selection_sort([5, 2, 1, 6, 9, 7, 8]))
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    status = True
    while status:
        status = False
        for i in range(len(arr) - 1):
            r = i + 1
            if arr[i] > arr[r]:
                arr[i], arr[r] = (arr[r], arr[i])
                status = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
