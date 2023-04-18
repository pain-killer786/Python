# Input a,b,c of a quadratic equation and find it's roots

a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if (b*b-4*a*c)<0:
    x1=(-b+abs(b*b-4*a*c)**0.5)/2*a
    x2=(-b-abs(b*b-4*a*c)**0.5)/2*a
    print(x1,";",x2)
else:
    x1=(-b+(b*b-4*a*c)**0.5)/2*a
    x2=(-b-(b*b-4*a*c)**0.5)/2*a
    print(x1,"i","x",x2,"i")