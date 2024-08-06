
# function to count the strings
def count_strings(list_of_strings):
    count = 0
    for string in list_of_strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count


list_of_strings = ['abc', 'xyz', 'aba', '1221']
result = count_strings(list_of_strings)
print(result) 
