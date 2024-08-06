#find list of words longer than n from list
def find_long_words(n, list):
    for i in list:
        if len(i) > n:
            print(i)
        else:
            print('No words found')    
find_long_words(5, ["apple", "banana", "cherry"])            
        