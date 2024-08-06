#remove duplicates from list
def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
            
    print(new_list)
remove_duplicates([1,2,3,3,4,5,5])