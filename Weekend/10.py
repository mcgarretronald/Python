# Find common items between two lists
list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9]

# Use list comprehension to check if each item in list_a is in list_b
common_items = [i for i in list_a if i in list_b]

# Print the common items
print(common_items)

