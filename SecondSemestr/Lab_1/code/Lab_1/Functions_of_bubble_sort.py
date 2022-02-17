import random
import matplotlib.pyplot as plt


def show_a_functional_graph_of_bubble_sort():
    # Build a function graph
    plt.show()


def get_number_of_swaps(n):
    counter = 0
    for i in range(1, n):
        counter = counter + i
    return counter


def add_not_sorted_array(x):
    y = []
    for i in x:
        number_of_switches = get_number_of_swaps(i)
        y.append(random.randint(0, number_of_switches))
    plt.plot(x, y, label='Not sorted array', color='blue')


def add_sorted_array(x):
    y = []
    for i in range(len(x)):
        y.append(0)
    plt.plot(x, y, label='Sorted array', color='green')


def add_reverse_sorted_array(x):
    y = []
    for i in x:
        number_of_switches = get_number_of_swaps(i)
        y.append(number_of_switches)
    plt.plot(x, y, label='Reverse sorted array', color='red')


def the_worst_complexity(x):
    y = []
    for i in x:
        y.append(i**2)
    plt.plot(x, y, label='The worst complexity', color='purple')


def the_best_complexity(x):
    y = []
    for i in x:
        y.append(i)
    plt.plot(x, y, label='The best complexity', color='yellow')


# Input array
x = [10, 100, 1000, 5000, 10000, 20000, 50000]

# Set setting for functional graph
plt.figure()

plt.subplot(1, 2, 1)
plt.title('Functions of bubble sort executions')
plt.ylabel('Number of swaps')
plt.xlabel('Number of elements')

# Not sorted array
add_not_sorted_array(x)

# Sorted array
add_sorted_array(x)

# Reverse sorted array
add_reverse_sorted_array(x)

plt.legend()

plt.subplot(1, 2, 2)
plt.title('Functions of bubble sort executions')
plt.ylabel('Iterations')
plt.xlabel('Number of elements')

# The worst complexity of switches in bubble sort
the_worst_complexity(x)

# The best complexity of switches in bubble sort
the_best_complexity(x)

plt.legend()
