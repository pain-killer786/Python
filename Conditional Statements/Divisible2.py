# Input a number and find whether it is divisible by 5 and 2 or 3 

a=int(input("Enter a number"))
if a%5==0 and a%2==0:
    print("Divisible by 5 and 2")
elif a%3==0:
    print(("Divisible by 3"))
else:
    print("Not")