x = int(input("enter x: "))
y = int(input("enter b: "))
a = int(input("enter a: ")) 

if 15<x<45 and 25<y<55:
    if a>100 and a%7 == 0:
        print ("authorized core access")
    else:
        print("securtiy alert: core violation")
elif 10<x<50 and 20<y<60:
    if a%2 == 0 or x == y:
        print("permitted perimeter pass")
    else:
        print("warning: perimeter check required")
else:
 print("safe: free navigation")

