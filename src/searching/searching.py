def linear_search(arr, target):
    # Your code here


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    lowest = 0
    highest = len(arr) - 1

    while lowest <= highest:
        middle = lowest + (highest - lowest) // 2

        print('middle: ', middle)

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            highest = middle - 1 
        elif arr[middle] < target:
            lowest = middle + 1

    return -1  # not found
