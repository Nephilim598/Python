import math
from turtle import *
from random import *

'''

a1 = int(input("szam1"))                   # Feladat_01
a2 = int(input("szam2"))


if a1>=0 and a2>=0:
    print("mind2 poz.")
elif a1 == 0 or a2 == 0:
    print("Egyik értéke 0")
elif a1 == 5 or a2 == 4:
    if a1 == 5:
        print("elsoszam = 5")
    else:
        print("masodik = 4")
elif a1 <= 5 or a2 >= 13:
    if a1 <= 5:
        print("elsoszam kisebb 5")
    elif a2 >= 13:
        print("masodik nagyobb 13")
elif a1 > 0 and a2 < 0 or a2 > 0 and a1 < 0:
    if a1 > 0 and a2 < 0:
        print("elso a poz")
    elif a2 > 0 and a1 < 0:
        print("masodik poz")
else:
    print("Hiba! ")           

'''

'''

a = int(input("számot:"))


if a%10 == 0:
    print("osztható 10-zel")                  # Feladat_03

'''

'''

a = int(input("számláló:"))
b = int(input("nevező:"))

if b <= 0:
    print("nem jó")

else:
    print("Oké")                               


'''


'''

a = int(input("számot"))

b = math.floor(a / 100)
b2 = b * 100
c = math.floor(a - b2 )
c2 = c % 10
c3 = math.floor((c - c2) / 10)
d = math.pow(b,3) + math.pow(c3,3) + math.pow(c2,3)                # Feladat_05

if a == d:
    print("Az",a,d)
else:
    print("Nem az",a,d)

'''

'''

a = int(input("számot:"))

if a == 4:
    print("A szám a 4-es!")
else:
    print("-")

if a < 10:
    print("Kisebb mint 10")
else:
    print("-")
if a > 0:
    print("páros")
else:
    print("-")
if 0<a<10:
    print("0-10 közé esik")
else:
    print("-")
if a % 5 == 0 and a % 3 == 0:
    print("osztható 5-tel és 3-mal")
else:
    print("-")
if 10<a<20:
    print("-")
else:
    print("nem esik 10-20 közé")                       # Feladat_06


'''

'''

a = int(input("számot1:"))
b = int(input("számot2:"))

if a == b:
    print("-")
else:
    print("A két szám nem egyenlő")
if a<0 and  b<0:
    print("mind2 negatív")
else:
    print("-")
if a%3 == 0 or  b%3 == 0:
    print("egyik osztható 3-mal")
else:
    print("-")
if a<0 and b>0 or b<0 and a>0:
    print("egyik poz. másik neg.")
else:
    print("-")

if a % 2 == 0 and b % 2 == 0:
    print("páros")
elif a % 4 == 0 and b % 4 == 0:
    print("páros")
elif a % 6 == 0 and b % 6 == 0:
    print("páros")
elif a % 8 == 0 and b % 8 == 0:
    print("páros")
else:
    print("páratlan")

'''

'''

a = int(input("A és C oldal:"))
b = int(input("B és D oldal:"))

if a == b:
	print("négyzet")
else:
	print("téglalap")

for i in range(2):
	forward(math.pow(a,2))
	right(90)
	forward(math.pow(b,2))
	right(90)                                           # Feladat_08

'''

'''

a = int(input("A oldal:"))
b = int(input("B oldal:"))
c = int(input("C oldal:"))

if a == b and a==c:
	print("egyenloszáru 3szg")
else:
	print("nem egyenlo 3szg")                                    # Feladat_09


'''

'''

a = int(input("számot:"))

if a == 10:
    print("egyenlő 10-zel")
elif a == 100:
    print("egyenlő 100-zal")
elif a == 1000:
    print("egyenlő 1000-rel")
else:
    print("Nem 10/100/1000!")              # Feladat_10

'''

'''

a = int(input("számot:"))


if 1<= a <=9:
    print("Benne van!")
else:
    print("Nincs benne!")                   # Feladat_11

'''

'''

a = int(input("számot:"))


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
    print("páratlan")                # Feladat_12

'''

'''

a = int(input("számot1:"))
b = int(input("számot2:"))

if (b % a) == 0:
    print("osztója az 1. a 2.-nak")
else:
    print("Nem osztója")                   # Feladat_13

'''

'''

a = int(input("számot1:"))

if a > 0:
    print(math.sqrt(a))             # Feladat_14
else:
    print("a gyökvonás csak nem negatív számok esetén értelmezett művelet")

'''

'''

a = int(input("számot1:"))
b = int(input("számot2:"))
c = int(input("számot3:"))

if a + b > c: 
    print(a+b+c)
elif a + c > b: 
    print(a+b+c)
elif b + c > a: 
    print(a+b+c)
else:
    print("Hiba!")                 # Feladat_15

'''

'''

a = int(input("KM:"))
b = int(input("Min:"))

a = a * 1000
b = b * 60

print(a / b,"KM/H")               # Feladat_16

'''

'''

a = int(input("számot:"))

if a > 0:
    print("+%d" % (a))
elif a == 0:
    print("+-%d" % (a))
elif a < 0:
    print(a)
else:
    print("Hiba!")                  # Feladat_17

'''

'''

a = int(input("hőmérséklet: "))

if a < 0:
    print("szilárd (jég)")
elif 0 < a < 100:
    print("folyékony (víz)")
elif 100 <= a:                         # Feladat_19
    print("légnemű (gőz)")                 
else:
    print("Hiba!")

'''

'''


a = int(input("(x,y) add meg x-et:"))
b = int(input("(x,y) add meg y-t:"))

if a>0 and b>0:
    print("1.")
elif a<0 and b>0:
    print("2.")
elif a<0 and b<0:
    print("3.")
elif a>0 and b<0:
    print("4.")
else:
    print("Hiba!")                        # Feladat_20

'''

'''

a = int(input("0-100-ig pontok:"))

if 0 < a <= 42:
    print("elégtelen")
elif 43 < a <= 57:
    print("elégséges")
elif 58 < a <= 72:
    print("közepes")
elif 72 < a <= 87:
    print("jó")
elif 88 < a <= 100:
    print("jeles")
else:
    print("Hiba")                             # Feladat_21

'''

'''

a = int(input("korod:"))

if 0 < a <= 42:
    print("gyerek")
elif 43 < a <= 57:
    print("tini")
elif 58 < a <= 72:
    print("fiatal")
elif 72 < a <= 87:
    print("felnőtt")
elif 88 < a <= 100:
    print("öreg")
else:
    print("Hiba")                      # Feladat_22

'''

'''

a = int(input("tárgy:"))
b = int(input("folyadék:"))


if a > b:
    print("elmerül")
elif a < b:
    print("úszik")
elif a == b:
    print("lebeg")
else:
    print("Hiba")                        # Feladat_23

'''

'''

a = int(input("hiányzásod:"))
b = int(input("korod:"))

if b >= 18:
    print("felszólítás kiküldése szükséges")
else:
    print("szülői értesítés szükséges")

if a == 0:
    print("5")
elif 1<= a <= 3:
    print("4")
elif 4<= a <= 9:
    print("3")
elif 10<= a:
    print("2")
else:
    print("Hiba")                    # Feladat_24

'''

'''

k = ord(input("karaktert:"))

a = k + 32 
b = k - 32
if 48 <= k <=57:
	print(chr(k),"szám","\n ascii kodja:",k)
elif 65<= k <= 90:
	print(chr(k),"-->nagybetu","\n ascii kodja:",k,"\n masik formaja:",chr(a))
elif 97<= k <= 122:
	print(chr(k),"-->kisbetu","\n ascii kodja:",k,"\n masik formaja:",chr(b))
else:
	print(chr(k), "-->egyeb", "\n ascii kodja:", k)                                    # Feladat_25

'''

'''

a = int(input("km/h:"))

if 0 < a <= 1:
    print("csiga")
elif 1 < a <= 6:
    print("csuka")
elif 7 < a < 32:
    print("bálna")
elif 32 <= a < 48:
    print("sirály")
elif 48 <= a <= 64:
    print("nyúl")
elif 65 <= a <= 70:
    print("strucc")
elif 71 <= a <= 110:
    print("gepárd")
elif 111 <= a <= 320:
    print("sólyom")
else:
    print("Hiba")                   # Feladat_26

'''

'''

a = int(input("km:"))

if 1 <= a <= 2:
    print("500Ft")
elif 3 <= a <= 5:
    print("700Ft")
elif 6 <= a <= 10:
    print("900Ft")
elif 11 <= a <= 20:
    print("1400Ft")
elif 21 <= a <= 30:
    print("2000Ft")
else:
    print("Hiba!")                      # Feladat_27

'''

'''

a = int(input("szélesség:"))
b = int(input("hosszúság:"))
c = int(input("adó:"))

if a<=15:
    print("jár a kedvezmény! új adó:",c*0.20)
elif  b<=25:
    print("jár a kedvezmény! új adó:",c*0.20)            # Feladat_28
else:
    print("No,no,no")

'''

'''

T = int(input("(1800<=T<=2099)évszámot:"))

A = T / 19 
B = T / 4  
C = T / 7  
D = ( 19 x A + 24 ) / 30
E = ( 2 x B + 4 x C + 6 x D + 5 ) / 7 
H = 22 + D + E

if H <= 31:
    print("húsvét vasárnap")                    #29  NINCS KÉSZ

'''

'''

a = int(input("1-5 jegyet:"))

if a == 5:
    print("ötös")
elif a == 4:
    print("négyes")
elif a == 3:
    print("hármas")
elif a == 2:
    print("kettes")
elif a == 1:
    print("egyes")
else:
    print("Hiba! Rossz érték!")                     # Feladat_30

'''

'''

a = int(input("1-7 hét napja:")


if a == 1:
    print("Hétfő")
elif a == 2:
    print("Kedd")
elif a == 3:
    print("szerda")
elif a == 4:
    print("csütörtök")
elif a == 5:
    print("péntek")
elif a == 6:
    print("szombat")
elif a == 7:
    print("vasárnap")                          # Feladat_31

'''

'''

a = randrange(1,7)

if 1 <= a <= 2:
    print("Gyenge")
elif 3 <= a <= 4:
    print("Nem rossz")
elif 5 <= a:
    print("jó")
elif 6 <= a:
    print("kiváló")
else:
    print("Hiba!")                        # Feladat_33

'''










































































