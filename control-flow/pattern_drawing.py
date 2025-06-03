size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Loop through each row
while row < size:
    # Print each column in the row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
    












