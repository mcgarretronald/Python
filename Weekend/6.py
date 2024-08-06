def calculate_difference(list1, list2):
    list_diff = []
    list_intersection = []
    for element in list1:
        if element in list2:
            # If it is, add it to the intersection list
            list_intersection.append(element)
        else:
            # If it's not, add it to the difference list
            list_diff.append(element)

    # Find the elements in list2 that are not in list1
    for element in list2:
        if element not in list1:
            list_diff.append(element)

    # Remove the elements that are in both lists from the difference list
    for element in list_intersection:
        if element in list_diff:
            list_diff.remove(element)

    return list_diff


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = calculate_difference(list1, list2)
print(result)
