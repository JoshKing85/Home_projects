import random

# Create a list of numbers from 1 to 9
numbers = list(range(1, 10))

# Shuffle the numbers randomly
random.shuffle(numbers)

# Arrange the numbers into a 3x3 2D array
two_d_array = [numbers[i:i+3] for i in range(0, 9, 3)]

# Print the 2D array
for row in two_d_array:
    print(row)