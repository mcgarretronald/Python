# Get frequency of items in list
def get_frequecy(freqlist):
    for i in freqlist:
        print(f'{i} : {freqlist.count(i)} times')
get_frequecy([1,2,3,3,3,3,4,5])        