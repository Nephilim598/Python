import random
from re import T

################    1-8-ig a feladatok sorrendben    ################
"""
#F01

for i in range(4):
	random.randint

for i in range(4):
	while()

"""

"""
#F02

szam=random.randint(0,2)
tipp=int(input("tippelj"))
while(tipp=szam)
	szam=random.randint(0,2)
	tipp=int(input("Nem talált! új tippet!"))
print("Siker")

"""

"""
#F03


szam=int(input("szamot!"))
eredmeny=szam
while(szam!=0):
	szam=int(input("új szamot!"))
	eredmeny=eredmeny*szam
	print(eredmeny)
print("vége")

"""

"""
#F04

szavak="alma"
ujszo=input("újszó")
while(ujszo!=""):
	szavak=szavak+" "+ujszo
	print(szavak)
	ujszo=input("újszó")

"""

"""

#F06

i=int(input("darab"))
k=input("karakter")
a = ""
while(i!=0):
	a=a+k
	i=i-i
print(a)

"""

"""

#F07


a=int(input("a"))
b=int(input("b"))
i=int(input("lépés"))
s=""

if(a>b):
	i=-1

s+=str(a)

while(a!-b):
	a+=1
	s+=", "+str(a)
print(s)

"""

"""
#F08

i=1
while(i<1000):
	if(i%3==0):
		if(i%5==0):
			print(i)

	i=i+1

"""
################    #################################    ################
# Korrepesekkel

# F20
'''
while True:
    n=int(input("Kérek egy számot: "))
    if(n%2==0):
        print("A megadott szám megfelelő")
        break
'''

# F21
'''
while True:
    n=int(input("Kérek egy számot: "))
    if(n>0):
        print(n%5)
        break
'''

# F22
'''
while True:
    n=int(input("Kérek egy számot 1-7 között: "))
    if(1<=n<=7):
        if(n==1):
            print("hétfő")
        elif(n==2):
            print("kedd")
        elif(n==3):
            print("szerda")
        elif(n==4):
            print("csütörtök")
        elif(n==5):
            print("péntek")
        elif(n==6):
            print("szombat")
        else:
            print("vasárnap")
        break
'''

# F23
'''
while True:
    n=int(input("Kérek egy számot: "))
    if(n>0 or n%2==0):
        print("Hiba!")
    else:
        break
'''

# F24
'''
while True:
    n=int(input("Kérek egy számot: "))
    if(n%3==0 and n%5==0):
        print(n/3, n/5, sep=' ')
        break
'''

# F25
'''
while True:
    n=int(input("Kérek egy számot: "))
    if(n==0):
        break
    else:
        print(n%5)
'''

# F26
'''
while True:
    a=int(input("a="))
    b=int(input("b="))
    if(a==b):
        break
    elif(a>b):
        print("a nagyobb mint b")
    else:
        print("b nagyobb mint a")
'''

# F27
'''
while True:
    n=random.randint(1,12)
    print(n, n%3, sep=' ')
    m=chr(ord(input("Új szám? (i/n) ")))
    if m=='n':
        break
'''

# F29
'''
n=random.randint(1,50)


while True:
    tipp=int(input("Tipp: "))
    if(tipp==n):
        break
    elif(tipp<n):
        print("A gondolt szám nagyobb")
    else:
        print("A gondolt szám kissebb")
'''























