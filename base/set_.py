#!/usr/bin/python3

# In Python, a set is an unordered collection of unique elements. 
# It is mutable, but its elements must be immutable (e.g., numbers, strings, or tuples). 
# Sets are useful for removing duplicates, 
# performing mathematical set operations like union, intersection, and difference.

# Create empty set
my_set = set()

# No Duplicates: Duplicate elements are automatically removed.
my_set = {1,2,2,3,4,5}
print(my_set)

# Unordered: Elements have no specific order and cannot be accessed by index.

# Add a single element
my_set.add(6)

# Using remove. Raises an error if the element doesn't exist.
my_set.remove(3)

# Using discard. Doesn't raise an error if the element doesn't exist.
my_set.discard(3)

# Using pop. Removes and returns an arbitrary element.
my_pop = my_set.pop()
print(my_pop)
print(my_set)

# Using clear. Removes all elements from the set.
my_set.clear()
print(my_set)

# Union (| or union). Combines all unique elements from two sets.
set1 = {1,2,3}
set2 = {3,4,5}
print(f"=== {set1} === {set2} ===")
print(set1 | set2)

# Intersection (& or intersection). Finds common elements between two sets.
print(set1 & set2)

# Difference (- or difference). Finds elements in the first set but not in the second.
print(set1 - set2)

# Symmetric Difference (^ or symmetric_difference). Finds elements in either set but not both.
print(set1 ^ set2)

# Checking Membership
print(1 in set1)
print(6 in set2)

# Iterating Over a Set
for item in set1:
    print(item)
