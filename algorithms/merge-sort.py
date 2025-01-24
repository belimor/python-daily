#!/usr/bin/python3

# Concept: Divides the array into halves, sorts each half, and then merges them.
# Time Complexity: O(NlogN)

def merge_sort(arr):
    if len(arr) > 1:
        print("+++ arr:",arr)
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        print("left:", left, "right:", right)

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            print("=== start ===")
            print("arr:",arr)
            print("i:",i,"j:",j,"k:",k)
            print("arr[k]:",arr[k],"left[i]:",left[i],"right[j]:",right[j])
            if left[i] < right[j]:
                print("left[i] < right[j]: arr[k] = left[i]")
                arr[k] = left[i]
                print("arr[k]:", arr[k])
                i += 1
            else:
                print("else: arr[k] = right[j]")
                arr[k] = right[j]
                print("arr[k]:", arr[k])
                j += 1
            k += 1
            print("i:",i,"j:",j,"k:",k)
            print("arr:",arr)
            print("=== end ===")

        while i < len(left):
            print("- - - i:", i, "- - -")
            arr[k] = left[i]
            print("arr[k] = left[i]:", arr[k])
            i += 1
            k += 1

        while j < len(right):
            print("- - - j:", j, "- - -")
            arr[k] = right[j]
            print("arr[k] = right[j]:", arr[k])
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Merge Sorted:", arr)  # Output: [5, 6, 7, 11, 12, 13]
