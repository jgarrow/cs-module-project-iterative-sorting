# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    print('arr: ', arr)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    # if there are less than 2 elements, there's nothing to swap
    if len(arr) < 2:
        return arr

    curr_index = 0
    swapped = True

    while swapped is True:
        # reset the index to zero after going through the whole list
        curr_index = 0

        # will still finish this whole block of code
        # if swapped is still False at the end, it will exit this while loop
        swapped = False

        # check if the curr_index and it's next increment both exist in the list
        while curr_index < len(arr) and curr_index + 1  < len(arr):
            
            # if the next element is smaller than the current one, swap them
            if arr[curr_index + 1] < arr[curr_index]:
                # temporary variable to hold on to what the current next element is
                curr_next = arr[curr_index + 1]

                # set the next element to our current index's element
                arr[curr_index + 1] = arr[curr_index]

                # set the current index value to the next element that we held onto
                arr[curr_index] = curr_next
                swapped = True

            # move onto the next pair
            curr_index += 1

    # print('arr: ', arr)

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
