import time


def cocktail_sort():
    sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
    for size in sizes:
        filename = f"numbers_{size}.txt"

        # Read numbers from input file
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]

        # Start the timer
        start_time = time.time()

        # Perform cocktail sort
        numbers_length = len(numbers)
        swapped = True
        start = 0
        end = numbers_length - 1

        while swapped:
            swapped = False

            for i in range(start, end):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True

            start += 1

        # Stop the timer
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(
            f"Cocktail sort for file '{filename}' took {elapsed_time:.6f} seconds.")
