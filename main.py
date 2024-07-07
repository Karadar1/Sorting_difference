from generate_numbers import generate_numbers
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from radix_sort import radix_sort
from cocktail_sort import cocktail_sort


def display_menu():
    while True:
        print("\nMenu:")
        print("1. Generate file for 100, 1000, 10000, 100000, 1000000, 10000000 numbers")
        print("2. Bubble sort")
        print("3. Merge sort")
        print("4. Quick sort")
        print("5. Heap sort")
        print("6. Insertion sort")
        print("7. Selection sort")
        print("8. Radix sort")
        print("9. Cocktail sort")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            generate_numbers()
        if choice == '2':
            bubble_sort()
        if choice == '3':
            merge_sort()
        if choice == '4':
            quick_sort()
        if choice == '5':
            heap_sort()
        if choice == '6':
            insertion_sort()
        if choice == '7':
            selection_sort()
        if choice == '8':
            radix_sort()
        if choice == '9':
            cocktail_sort()
        elif choice == '10':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    display_menu()
