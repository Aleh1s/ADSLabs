from Array_helper import *


# Output a menu
print_menu()

# Input a choice
choice = int(input('Choice: '))

# Validation a choice
is_choice_valid(choice)

# Input data
range_of_array = int(input('Write a range of array: '))

# Generating an array
array = generate_array_from_range(range_of_array)

# Array before sorting
print('Array before sorting:\n' + str(array))

# Sorting and output
do_choice(choice, array, range_of_array)

# Print a functional graph
print_functional_graphs()



