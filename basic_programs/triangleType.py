a=int(input("angle 1 "))
b=int(input("angle 2 "))
c=int(input("angle 3 "))
total=a+b+c
if a==b and b==c and total==180:
    print('equilateral traingle')
elif a==b or a==c or b==c and total==180:
    print('isoceles traingle')
elif a!=b and a!=c and b!=c and total==180:
    print("scalene triangle")
else:
    print("not a triangle")    
            