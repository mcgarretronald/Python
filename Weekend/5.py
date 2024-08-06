# Check if nu ber in list is prime
def check_if_prime(primelist):
    for num in primelist:
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
    return True  


numbers = [3, 5, 7, 13] 
print(check_if_prime(numbers)) 
