#!/usr/bin/python3

# Concept: Picks a pivot, partitions the array around it, and recursively sorts the partitions.

# Time Complexity: O(NlogN)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Quick Sorted:", sorted_arr)  # Output: [1, 5, 7, 8, 9, 10]

