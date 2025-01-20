#!/usr/bin/python3

# Concept: Builds the sorted array one item at a time by inserting elements in their correct position.

def insertion_sort(arr):
    print(arr)
    print("- - - - - -")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print("key:",key, "j:",j)
        while j >= 0 and key < arr[j]:
            print(str(key) + "<" + str(arr[j]))
            arr[j + 1] = arr[j]
            j -= 1
            print("j:",j)
            print(arr)
        arr[j + 1] = key
        print(arr)
        print("= = = =")

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Insertion Sorted:", arr)  # Output: [5, 6, 11, 12, 13]
