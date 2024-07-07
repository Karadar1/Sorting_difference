import time


def insertion_sort():
    sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
    for size in sizes:
        filename = f"numbers_{size}.txt"

        # Read numbers from input file
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]

        # Start the timer
        start_time = time.time()

        # Perform insertion sort
        for i in range(1, len(numbers)):
            key = numbers[i]
            j = i - 1
            while j >= 0 and key < numbers[j]:
                numbers[j + 1] = numbers[j]
                j -= 1
            numbers[j + 1] = key

        # Stop the timer
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(
            f"Insertion sort for file '{filename}' took {elapsed_time:.6f} seconds.")
