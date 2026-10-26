tier = input("enter your tier: ")
P = float(input())
T = float(input())
D = P
if tier == "Gold":
    D = P * 0.8
    if D > 400:
        D = D - 50
    elif int(P) % 2 == 0:
        D = D - 10
elif tier == "Silver":
    if P > 300:
        D = P * 0.85
    elif P >= 100 and P <= 300:
        D = P * 0.9
    else:
        D = P - 5
        if D < 0:
            D = 0
elif tier == "Bronze":
    if P > 150:
        if int(P) % 2 == 0:
            D = P * 0.93
        else:
            D = P * 0.95
    else:
        D = P
else:
    D = P

total = D + (D * T / 100)

print("{:.2f}".format(total))