import matplotlib.pyplot as plt
import random as ran


def show_a_functional_graph_of_combine_sort():
    # Build a function graph
    plt.show()


def add_function_of_sorted_array(x):
    y = []
    for i in x:
        y.append(0)
    plt.plot(x, y, label='Sorted array', color='green')


def add_function_of_reverse_sorted_array(x):
    y = []
    for i in x:
        y.append(i // 2)
    plt.plot(x, y, label='Reverse sorted array', color='red')


def add_function_of_not_sorted_array(x):
    y = []
    for i in x:
        y.append(ran.randint(0, i // 2))
    plt.plot(x, y, label='Not sorted array', color='blue')


def the_best_complexity(x):
    y = []
    for i in x:
        y.append(i)
    plt.plot(x, y, label='The best complexity', color='yellow')


def the_worst_complexity(x):
    y = []
    for i in x:
        y.append(i**2)
    plt.plot(x, y, label='The worst complexity', color='purple')


x = [10, 100, 1000, 5000, 10000, 20000, 50000]


plt.figure()

# Set setting for a first functional graph
plt.subplot(1, 2, 1)
plt.title('Functions of combine sort executions')
plt.ylabel('Number of swaps')
plt.xlabel('Number of elements')

# Not sorted array
add_function_of_not_sorted_array(x)

# Sorted array
add_function_of_sorted_array(x)
#
# Reverse sorted array
add_function_of_reverse_sorted_array(x)

plt.legend()

# Set setting for a second functional graph
plt.subplot(1, 2, 2)
plt.title('Algorithm complexity')
plt.ylabel('Iteration')
plt.xlabel('Number of elements')

# The worst complexity of switches in bubble sort
the_worst_complexity(x)

# The best complexity of switches in bubble sort
the_best_complexity(x)

plt.legend()
