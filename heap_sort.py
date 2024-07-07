import time


def heap_sort():
    sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
    for size in sizes:
        filename = f"numbers_{size}.txt"

        # Read numbers from input file
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]

        # Declare functions
        def _heap_sort(numbers, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and numbers[largest] < numbers[left]:
                largest = left

            if right < n and numbers[largest] < numbers[right]:
                largest = right

            if largest != i:
                numbers[i], numbers[largest] = numbers[largest], numbers[i]
                _heap_sort(numbers, n, largest)

        # Start the timer
        start_time = time.time()

        # Perform heap sort
        numbers_length = len(numbers)
        for i in range(numbers_length // 2 - 1, -1, -1):
            _heap_sort(numbers, numbers_length, i)

        for i in range(numbers_length - 1, 0, -1):
            numbers[i], numbers[0] = numbers[0], numbers[i]
            _heap_sort(numbers, i, 0)

        # Stop the timer
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(
            f"Heap sort for file '{filename}' took {elapsed_time:.6f} seconds.")
