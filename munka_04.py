from ctypes import cdll
import math
import random

'''
for i in range(0,51,1):
    print(i)

### ELVÁLASZTÓ! ### 

for i in range(182,213,1):
    print(i)

#

for i in range(100,201,1):
    print(i)

#

for i in range(89,56,-1):
    print(i)

#

for i in range(1,21,1):
    print(i,math.pow(i,2))

#

for i in range(99,0,-6):
    print(i-3)  

#

for i in range(101,50,-5):
    print(i-1,"Kétszerese:", (i-1)*2)

#

for i in range(1,1000,1):
    print(i,end=",") 
    if i == 999:
        print("1000",end=".")

#

for i in range(1000,0,-3):                         # Feladat_01
    print(i)

'''

'''

for i in range(1,101,1):                         
    print("*")

#

a = int(input("számot:"))
b = input("betűt:")
for i in range(0,a,1):                         
    print(b)

#

b = input("szöveget:")
a = len(b) + 4
for i in range(0,a,1):
    print( end="*")
print("\n*",b,"*")
for i in range(0,a,1):
    print( end="*") 

#

for i in range(0,9,1):
    print("*************************************************")
    print("*     *     *     *     *     *     *     *     *")
print("*************************************************")                            # Feladat_02

'''

'''

a = int(input("mettől:"))
b = int(input("meddig:"))
c = int(input("+- lépés:"))

if a < b:
    b = b + 1
    for i in range(a,b,c): 
        print(i)
elif a > b:
    b = b - 1
    for k in range(a,b,c): 
        print(k)
else:
    print("Hiba!")                                           # Feladat_03

'''

'''

a = int(input("DB:"))

y = 2
for i in range(0,a,1):
    
    y = y
    x = math.pow(y,2) 
    print(x,end=";")
    y = y + 1                                      # Feladat_04 

'''

'''

a = int(input("DB:"))

y = 2
for i in range(0,a,1):
    
    y = y
    x = math.pow(y,3) 
    print(x)
    y = y + 1                                     # Feladat_05

'''

'''

a = int(input("szám1:"))
b = int(input("szám2:"))

if a < b:
    for i in range(a,b):
        print(round(math.sqrt(i),2))
elif a > b:
    for i in range(b,a):
        print(round(math.sqrt(i),2))           # Feladat_06

'''

'''

a = int(input("számot:"))
print(math.factorial(a))                         # Feladat_07

'''

'''

a = int(input("DB:"))

y = 2
for i in range(0,a,1):
    
    y = y
    x = math.pow(y,2)                               # Feladat_08        
    print(x)
    y = y + 1 

'''

'''
a = int(input("számot:"))

if a % 2 == 0: 
    print("H")
elif a % 4 == 0:
    print("H")
elif a % 6 == 0:
    print("H")
elif a % 8 == 0:
    print("H")   
else:
    #for i in range(a,0,-1):
    #    print(x=math.pow(i))              #9
    print(a)
''' 


        

#####################################################################################
# TELÓN ÖSSZEDOBOTT
'''
k = int(input("számot:"))

x=0
y=1
z=0
if k > 0:
    for i in range(0, k, 1):
     x = z * y
     print(x)
     z += 1
     y = y + 1
else:
    print("hiba")                   # feladat 10

'''

'''
a = int(input("számot:"))
x=0

for i in range(0,a,1):
	b=3*(x+1)
	print(b)
	if a == b or a % b == 0:                #feladat 11
		print(b,"jó")

'''
'''
a = randrange(0,10)
b = randrange(0,25)
c = randrange(0,50)
d = randrange(10,75)
e = randrange(-50,50)
f = randrange(-100,-70)                   # f15
'''
'''
a = int(input("szám:"))
a=a+1
for i in range(0,a,1):
	print("*")

for i in range(0,a,1):
	print("\n*",a*" ","*")

for i in range(0,a,1):                     # f16
	print("*")

'''
'''
a = 1
for i in range(1,256,1):
	print(chr(a),odr(a))                    #f22
	a = a + 1
'''
'''

a=int(input(számot:))

if a % 2 == 0:
	print("2")
elif a % 3 == 0:
	print("3")
elif a % 4 == 0:
	print("4")
elif a % 5 == 0:
	print("5")
elif a % 6 == 0:
	print("6")
elif a % 7 == 0:
	print("7")
elif a % 8 == 0:
	print("8")
elif a % 9 == 0:                              #23
	print("9")

'''

'''

a = int(input("számot:"))
x=1
y=0
for i in range(1,10,1):
	if a%(x+1) ==0:
		y = (x+1) + y
      #  x +1
print(y)                                #24
'''

##############################################################################



# 2022-10-30  Gyakorlás alább


# F10

"""
k = int(input("számot: "))
x = int(input("hányszor: "))
for i in range(1,x):
    a = k + (k*(k+1))
    k = k+1
    
print(a)
"""

"""
N = int(input("számot: "))

for i in range(1,121):
    
    b = 3 * i
    if b <= N:
        print(b)
"""


"""
D = int(input("számot: "))
F = 0
F1 = 0
F2 = 1
for i in range(1,D):
    F = F1 + F2
    F1 = F2
    F2 = F
    print(F)
"""
"""
# kell egy számláló, logikai rész, és egy b += 1 rész ami ha N lesz break

N = int(input("DB? "))
b = 0
for i in range(0,10001):
    if i % 2 == 0:
        print()
    elif i % 3 == 0:
        print()
    elif i % 4 == 0:
        print()
    elif i % 5 == 0:
        print()
    elif i % 6 == 0:
        print()
    elif i % 7 == 0:
        print()
    elif i % 8 == 0:
        print()
    elif i % 9 == 0:
        print()
    else:
        print("Prímszám: ",i)
        b += 1
    if b == N:
        break

"""
"""

for i in range(1,11):
    for j in range(1,11):
        print(i * j, end=" ")
    print("")

"""

# hány feladat, két random szám 1-100 között, a két szám össszege és különbsége,
# a felhasználó által beírt két szám összege és különbségének az összehasonlítása,
# majd a helyes és helytelen tippek száma

DB = int(input("Hány feladatot?"))

T1 = 0
T2 = 0
for i in range(1,DB):
    a = random.randrange(1,101)
    b = random.randrange(1,101)
    c = abs(a - b) 
    d = a + b
    print("szám1: ",a, "szám2: ",b )
    ct = int(input("különbségük: "))
    dt = int(input("összegük: "))
    if c == ct:
        print("Helyes! kivonás")
        T1 += 1
    else:
        print("Helytelen! Újat!")
        T2 += 1
    if d == dt:
        print("Helyes! összeadás")
        T1 += 1
    else:
        print("Helytelen! Újat!")
        T2 += 1



















