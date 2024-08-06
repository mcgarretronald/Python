user = int(input('Enter a number: '))
# Check if the number is greater than 1
if user > 1:
    # Initialize a counter variable
    i = 2
    # Loop through numbers less than the user input
    while i < user:
        # Check if the user input is divisible by the counter
        if user % i == 0:
            # If it is, it is not a prime number
            print('Not a prime number')
            # Exit the loop
            break
        # Increment the counter
        i += 1
    else:
        # If the loop completes without finding a divisor, the number is prime
        print('Prime number')
else:

    print('Not a prime number')

