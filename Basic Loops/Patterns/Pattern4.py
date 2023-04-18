n=int(input("Enter a number"))
for i in range(0,n):
    for j in range(n,0,-1):
        if j>i+1:
            print(" ",end="")
        else:
            print("*",end="")
    print()