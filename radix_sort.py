import time


def radix_sort():
    sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
    for size in sizes:
        filename = f"numbers_{size}.txt"

        # Read numbers from input file
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]

        # Declare functions
        def counting_sort(numbers, exp):
            numbers_length = len(numbers)
            output = [0] * numbers_length
            count = [0] * 10

            for i in range(numbers_length):
                index = numbers[i] // exp
                count[index % 10] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = numbers_length - 1
            while i >= 0:
                index = numbers[i] // exp
                output[count[index % 10] - 1] = numbers[i]
                count[index % 10] -= 1
                i -= 1

            for i in range(numbers_length):
                numbers[i] = output[i]

        # Start the timer
        start_time = time.time()

        # Perform radix sort
        max_num = max(numbers)
        exp = 1
        while max_num // exp > 0:
            counting_sort(numbers, exp)
            exp *= 10

        # Stop the timer
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(
            f"Radix sort for file '{filename}' took {elapsed_time:.6f} seconds.")
