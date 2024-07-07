import time


def bubble_sort():
    sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
    for size in sizes:
        filename = f"numbers_{size}.txt"
        # Read numbers from input file
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]

        # Start the timer
        start_time = time.time()

        # Perform bubble sort
        numbers_length = len(numbers)
        for i in range(numbers_length):
            for j in range(0, numbers_length - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        # Stop the timer
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(
            f"Bubble sort for file '{filename}' took {elapsed_time:.6f} seconds.")
