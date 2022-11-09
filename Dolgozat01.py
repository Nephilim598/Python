import math

"""

a = float(input("Telek szélesség (m):"))
b = float(input("Telek magasság (m):"))

P = a * b
X = P / math.pow(5,2)
print(X,"csomagra van szükséged!")                     # Feladat_01

"""

"""

a = int(input("Adj egy számot: "))


if a > 0:
    print("pozitív")
else:
    print("Negatív")

if a % 2 == 0:
    print("páros")
elif a % 4 == 0:
    print("páros")
elif a % 6 == 0:
    print("páros")
elif a % 8 == 0:
    print("páros")
elif a % 10 == 0:
    print("páros")
else:
    print("páratlan")                                  # Feladat_02

"""

"""

a = int(input("Víz hőmérséklet: "))

if a < 0:
    print("szilárd (jég)")
elif 0 < a < 100:
    print("folyékony (víz)")
elif 100 <= a:                         
    print("légnemű (gőz)")                 
else:
    print("Hiba!")                                     # Feladat_03

"""

"""

a = int(input("Hány darab négyzetszámot kérsz: "))

y = 2
for i in range(0,a,1):
    
    y = y
    x = math.pow(y,2) 
    print("%.0f" % (x),end=";")
    y = y + 1                                          # Feladat_04

"""

"""

k = int(input("Adj egy értéket! K = "))
x = 0
for i in range(1,k+1):
    x += i * (i+1)
print(x)                                               # Feladat_05

"""
