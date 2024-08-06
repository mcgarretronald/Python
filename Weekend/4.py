#return true if list contain commmon item
def common_member(list_a, list_b):
#    for x in list_a:
#        for y in list_b:
#            if y == x:
#                print(True)
#            else:
#               print(False)
    return set(list_a)&set(list_b)
           
result =common_member([1,2,3,4,5], [5,6,7,8,9])    
print(bool(result))