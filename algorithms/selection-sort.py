#!/usr/bin/python3

# Concept: Repeatedly selects the smallest element and places it at the beginning.

def selection_sort(arr):
    print(arr)
    print("= = = = = = = =")
    for i in range(len(arr)):
        min_idx = i
        print(arr[min_idx])
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        print(arr[min_idx])
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Selection sorted arr:", arr)
