import time


def selection_sort():
    sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
    for size in sizes:
        filename = f"numbers_{size}.txt"

        # Read numbers from input file
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]

        # Start the timer
        start_time = time.time()

        # Perform selection sort
        for i in range(len(numbers)):
            min_index = i
            for j in range(i + 1, len(numbers)):
                if numbers[j] < numbers[min_index]:
                    min_index = j
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

        # Stop the timer
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(
            f"Selection sort for file '{filename}' took {elapsed_time:.6f} seconds.")
