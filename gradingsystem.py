# Promp user to enter 5 subjects
maths = input('Enter Maths Score: ')
english = input ('Enter English Score: ')
kiswahili = input ('Enter Kiswahili Score: ')
science = input ('Enter Science Score: ')
social = input ('Enter Social Score: ')

#Get Average
average = int(maths) + int(english) + int(kiswahili) + int(science) + int(social)
average =(average/5)
print( average)

bestPerformedSubject = max(maths, english, kiswahili, science, social)
print ( f'The best performed subject scored {bestPerformedSubject}')

if average >= 80:
    print ('A')
elif average >= 70:
    print('B')   
elif average >= 60:
    print('C')     
elif average >= 50:
    print('D')    
else:
    print('E')    
    