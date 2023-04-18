# Input a number and print all the numbers upto that number and from that number to 1

n=int(input("Enter a number"))
i=1
while(i<=n): #Loop to print in Forward Direction
    print(i, end=" ")
    i+=1
    
i=n
while(i>=1): #Loop to print in Backward Direction
    print(i, end=" ")
    i-=1