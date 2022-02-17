import numpy as np
import os
from Sort_algoritms import *
from Functions_of_bubble_sort import show_a_functional_graph_of_bubble_sort
from Functions_of_combine_sort import show_a_functional_graph_of_combine_sort


# Method for generating array with shuffled elements frtimeom range (n)
def generate_array_from_range(n):
    array = np.arange(1, n + 1)
    np.random.shuffle(array)
    return array

# Helper method to output data
def print_array(array, counter_of_swaps, counter_of_comparisons, time, range_of_array):
    # Calculate a delimiter
    delimiter = '---' * range_of_array if range_of_array < 18 else '----' * 18

    print(delimiter
          + '\nArray after sorting:\n' + str(array)
          + '\n'
          + delimiter
          + '\nNumber of switches: ' + str(counter_of_swaps)
          + '\nNumber of comparisons: ' + str(counter_of_comparisons)
          + '\nAlgorithm execution time: ' + str(time))

# To output menu
def print_menu():
    menu_delimiter = '-' * 28

    print('Choose a algorithm:\n'
          + menu_delimiter +
          '\n1) Bubble sort ( write: 1 )'
          '\n2) Combine sort ( write: 2 )'
          '\n' + menu_delimiter)

# To do choice
def do_choice(choice, array, range_of_array):
    if choice == 1:
        counter_of_swaps, counter_of_comparisons, time = bubble_sort(array)
        print_array(array, counter_of_swaps, counter_of_comparisons, time, range_of_array)
    elif choice == 2:
        counter_of_swaps, counter_of_comparisons, time = combine_sort(array)
        print_array(array, counter_of_swaps, counter_of_comparisons, time, range_of_array)
    else:
        print('Bad request!!!')


def print_functional_graphs():
    choice = input('Do you want to see functional graph? ( Y / N ): ')
    if choice == 'Y':
        show_a_functional_graph_of_bubble_sort()
        show_a_functional_graph_of_combine_sort()
    elif choice == 'N':
        print('Thank you!!!')
    else:
        exit('Bad request')


# Choice validator
def is_choice_valid(choice):
    if choice < 1 or choice > 2:
        exit('Bad choice!!!')