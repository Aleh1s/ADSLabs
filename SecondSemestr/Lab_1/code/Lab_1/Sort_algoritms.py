from timeit import default_timer as timer


# Algorithm bubble sort, asymptotic complexity O(n^2)
def bubble_sort(array):
    start_time = timer()
    counter_of_swaps = 0
    counter_of_comparisons = 0
    # Find the length of input data
    length = len(array)
    for i in range(0, length - 1):
        for j in range(0, length - i - 1):
            counter_of_comparisons = counter_of_comparisons + 1
            # Comparing two elements
            if array[j] > array[j + 1]:
                counter_of_swaps = counter_of_swaps + 1
                # Swapped elements
                array[j], array[j + 1] = array[j + 1], array[j]
    return counter_of_swaps, counter_of_comparisons, timer() - start_time


# Helper method for combine sort
def update_gap(gap):
    return gap - 1


# Algorithm combine sort, asymptotic complexity O(n^2)
def combine_sort(array):
    start_time = timer()
    counter_of_swaps = 0
    counter_of_comparisons = 0
    length = len(array)
    gap = length
    swapped = True
    # If gap (length) equals 1 or less return
    if gap < 2:
        return
    while gap > 1 or swapped:
        # Updated gap
        gap = update_gap(gap)
        swapped = False
        for i in range(0, length - gap):
            counter_of_comparisons = counter_of_comparisons + 1
            if array[i] > array[i + gap]:
                # Swapped the elements
                array[i], array[i + gap] = array[i + gap], array[i]
                counter_of_swaps = counter_of_swaps + 1
                swapped = True
    return counter_of_swaps, counter_of_comparisons, timer() - start_time


