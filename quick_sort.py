import time


def quick_sort():
    sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
    for size in sizes:
        filename = f"numbers_{size}.txt"
        # Read numbers from input file
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]

        # Declare functions
        def partition(arr, low, high):
            i = low - 1
            pivot = arr[high]

            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def _quick_sort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                _quick_sort(arr, low, pi - 1)
                _quick_sort(arr, pi + 1, high)

        # Start the timer
        start_time = time.time()

        # Perform quick sort
        _quick_sort(numbers, 0, len(numbers) - 1)

        # Stop the timer
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(
            f"Quick sort for file '{filename}' took {elapsed_time:.6f} seconds.")
