# Input two numbers and find sum, difference, multiplication and division based on user choice

a=int(input("Enter a choice: 1. Sum  2.Substraction 3.Multiplication 4.Division"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if a==1:
    print(b+c)
elif a==2:
    print(b-c)
elif a==3:
    print(b*c)
elif a==4:
    print(b/c)
else:
    print("Wrong choice")