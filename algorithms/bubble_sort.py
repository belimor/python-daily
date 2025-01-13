#!/usr/bin/python3

# The outer loop ensures all elements are eventually sorted.
# The inner loop compares adjacent elements and swaps them if they are out of order.
# After each pass of the outer loop, the largest unsorted element "bubbles up" to its correct position.

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, no need to compare them
        print("i:",i)
        for j in range(0, n - i - 1):
            print("j:",j)
            print(arr)
            print(arr[j], ">", arr[j+1])
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
            print("- - - - - -")

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", numbers)

bubble_sort(numbers)
print("Sorted array:", numbers)
