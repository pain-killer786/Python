num_rows = int(input("Enter a number"))

for i in range(num_rows):
    # Print spaces before the asterisks
    for j in range(i):
        print(" ", end="")
    
    # Print the asterisks
    for j in range(num_rows-i):
        print("*", end="")
    
    # Move to the next line
    print()
