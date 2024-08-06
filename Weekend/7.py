#Find second smallest number in a list
def find_second_smallest(numberlist):
    numberlist.sort()
    print( numberlist[1])
find_second_smallest([1,2,3,4,5,6,7,8,9,10])