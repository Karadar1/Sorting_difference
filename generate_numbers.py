import random


def generate_numbers():
    sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
    for size in sizes:
        filename = f"numbers_{size}.txt"
        numbers = random.sample(range(1, size + 1), size)
        with open(filename, "w") as file:
            for number in numbers:
                file.write(f"{number}\n")
        print(f"File '{filename}' has been created with {size} random numbers.")
