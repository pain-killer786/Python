# Input n numbers and count even,odd,positive and negative separately

n=int(input("Enter a number"))
cp=0;cn=0;co=0;ce=0
i=1
for  i in range(1,n+1):
    x=int(input("Enter a number"))
    if x>0:
        cp+=1
    if x<0:
        cn+=1
    if x%2==0:
        ce+=1
    if x%2!=0:
        co+=1
print(cp,cn,ce,co)
