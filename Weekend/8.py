#Get unique values from list
def unique_values(valuelist):
    new_list =[]
    for i in valuelist:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(unique_values([1,2,3,3,3,3,4,5]))
    