#Input the angles of a triangle and find the type of triangle

a=int(input("Enter an angle"))
b=int(input("Enter an angle"))
c=int(input("Enter aan angle"))
if a==90 or b==90 or c==90:
    print("Right angled Triangle")
elif a<90 or b<90 or c<90:
    print("Acute angled Triangle")
else:
    print("Obtuse angled Triangle")