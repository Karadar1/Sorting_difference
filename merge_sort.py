import time


def merge_sort():
    sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
    for size in sizes:
        filename = f"numbers_{size}.txt"

        # Read numbers from input file
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]

        # Declare functions
        def merge(left, right):
            merged = []
            while left and right:
                if left[0] <= right[0]:
                    merged.append(left.pop(0))
                else:
                    merged.append(right.pop(0))
            merged.extend(left or right)
            return merged

        def _merge_sort(numbers):
            if len(numbers) <= 1:
                return numbers

            mid = len(numbers) // 2
            left_half = _merge_sort(numbers[:mid])
            right_half = _merge_sort(numbers[mid:])

            return merge(left_half, right_half)

        # Start the timer
        start_time = time.time()

        # Perform merge sort
        sorted_numbers = _merge_sort(numbers)

        # Stop the timer
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(
            f"Merge sort for file '{filename}' took {elapsed_time:.6f} seconds.")
