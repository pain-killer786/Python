# Input time in seconds and convert it to HH:MM:SS
s=int(input("Enter time in seconds"))
h1=s/3600
h2=s%3600
m1=h2/60
m2=h2%60
s1=m1%60
s2=m2%60
print(int(h1), ":", int(m1), ":", int(s1))