def print_pattern(pattern_type, n):
    if pattern_type == 'triangle':
        for i in range(1, n + 1):
            print("*" * i)
    elif pattern_type == 'square':
        for i in range(n):
            print("*" * n)
    elif pattern_type == 'right_triangle':
        for i in range(1, n + 1):
            print(" " * (n - i) + "*" * i)
    elif pattern_type == 'diamond':
        for i in range(1, n + 1):
            print(" " * (n - i) + "*" * (2 * i - 1))
        for i in range(n - 1, 0, -1):
            print(" " * (n - i) + "*" * (2 * i - 1))
    elif pattern_type == 'checkerboard':
        for i in range(n):
            for j in range(n):
                if (i + j) % 2 == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    else:
        print("Invalid pattern type")

# Get user input for pattern type and size
pattern_type = input("Enter pattern type (triangle/square/right_triangle/diamond/checkerboard): ")
size = int(input("Enter size: "))

# Call the function to print the selected pattern
print_pattern(pattern_type, size)
