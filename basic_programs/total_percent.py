m1=int(input("marks in biology"))
m2=int(input("marks in chemistry"))
m3=int(input("marks in physics"))
m4=int(input("marks in mathmatics"))
m5=int(input("marks i camputer"))
total=m1+m2+m3+m4+m5
percentage=total*0.2
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=70:
    print("Grade C")
elif percentage>=60:
    print("Grade D")
elif percentage>=40:
    print("Grade E")
else:
    print("grade F")
    