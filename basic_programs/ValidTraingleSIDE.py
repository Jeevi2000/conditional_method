a=int(input("angle 1 "))
b=int(input("angle 2 "))
c=int(input("angle 3 "))
if a+b>c and b+c>a and a+c>b:
    print("Valid traingle")
else:
    print("invalid triangle")    