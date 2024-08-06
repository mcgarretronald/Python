# def getPower(a,b):
#     return print( a**b)
# getPower(2,3)

# NUMBER TWO
def LetterCounter(a):
    letters = {}
    for x in a:
        if x in letters:
            letters[x] += 1
        else:
            letters[x] = 1
    print(letters)
    
LetterCounter("Hello")
