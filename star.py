# Asks the user for the number of rows
rows = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(1, rows + 1):
    # Print spaces for the first row. Subtract i from rows to move left, 
    # multiply by 2 and subtract i to reduce the number of asterisks 
    print(' ' * (rows - i) + '*' * (2 * i - 1))

