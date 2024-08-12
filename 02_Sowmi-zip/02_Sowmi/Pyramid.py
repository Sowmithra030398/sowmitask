
def print_number_pyramid(height):
    number = 1
    for i in range(1, height + 1):
        # Print leading spaces
        print(' ' * (height - i), end='')
        # Print numbers
        for j in range(i):
            print(number, end=' ')
            number += 1
        print()  # Move to the next line

# Print the number pyramid
print_number_pyramid(6)
