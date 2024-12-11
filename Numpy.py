'''
Author: Joshil S Abraham
Date: 06/10/2024
Description: Program to create, append, and remove lists in Python using NumPy.
'''
import numpy as np

# Create a NumPy array (similar to a list)
array = np.array([1, 2, 3])
print("Original array:", array)

# Append elements to the array
# Note: np.append creates a new array with the added elements
array = np.append(array, [4, 5])
print("Array after appending elements:", array)

# Remove an element from the array
# Note: Use np.delete for removing elements
array = np.delete(array, 2)  # Removes the element at index 2
print("Array after removing the third element:", array)

# Create a new list from NumPy array
list_from_array = array.tolist()
print("Converted to Python list:", list_from_array)

# Append to the list
list_from_array.append(6)
print("List after appending:", list_from_array)

# Remove from the list
list_from_array.remove(4)
print("List after removing '4':", list_from_array)
