import math

'''
a = int(input("Hány Ft 1Kg kolompér? -->"))
b = int(input("Hány Kg krumpli kell? -->"))

print("Ennyi pénz kell magadddal vinned: %d Ft" % (a*b))    # Feladat_01
'''

'''
a = float(input("Fizetésed:"))
b = float(input("Emelkedési %:"))
b = b / 100
x = a * b
print("Új zsetonod: %.f Ft" % (a + x))               # Feladat_02
'''

'''
a = int(input("félretett pénz havonta:"))
b = int(input("laptop ár:"))

x = b / a
print("hónap:",math.ceil(x))                    # Feladat_03
'''

'''
a = float(input("Hitel összeg:"))
b = int(input("Futamidő:"))

x = a / b
print("Havi törlesztés: %.1f" % (x))              # Feladat_04
'''

'''
a = float(input("szélesség méter:"))
b = float(input("magasság méter:"))

P = a * b
x = P / 10
a = P + x
print(a,"m2 csempét kell vásárolnunk.")        # Feladat_05

# https://www.merkurymarket.hu/szakemberek-tippei/hogyan-kell-kiszamitani-a-csempeszamot-a-furdoszobaban,665.html#Hogyan%20sz%C3%A1m%C3%ADtsuk%20ki,%20h%C3%A1ny%20csempe%20sz%C3%BCks%C3%A9ges%20egy%20f%C3%BCrd%C5%91szob%C3%A1hoz?

'''

'''

a = int(input("időpont 1(óra):"))
b = int(input("időpont 1(perc):"))
c = int(input("időpont 1(másodperc):"))
x = int(input("időpont 2(óra):"))
y = int(input("időpont 2(perc):"))
z = int(input("időpont 2(másodperc):"))

a = a - x
b = b - y
c = c - z

a = a * 60 * 60
b = b * 60
i = a + b + c
print(i,"másodperc különbség")     # Feladat_06

'''

'''

A = int(input("Átmérő(cm):"))
B = int(input("Darab:"))

K = A * math.pi * 2
X = K * B + 60
print("%d cm szalag kell %d Db-hoz" % (X,B))            # Feladat_07

# https://hu.khanacademy.org/math/az-algebra-alapjai/x17cf222d75f5bcf0:az-alapok/x17cf222d75f5bcf0:a-kor-kerulete-es-terulete/a/radius-diameter-circumference

'''

'''
a = float(input("szélesség méter:"))
b = float(input("magasság méter:"))

P = a * b
X = P / math.pow(5,2)
print(X,"csomag kell")                  # Feladat_08

'''

'''

A = int(input("szám 1:"))
B = int(input("szám 2:"))

print("%.1f" % (math.sqrt(A + B)))          # Feladat_09

'''

'''

A = float(input("számot:"))

b = math.floor(A)
c = math.ceil(A)
d = round(A)
e = A - math.floor(A)

print("A megadott szám a ",b," és a ",c," egész számok között van, és ezek közül a ",d," számhoz van közelebb. A szám egész része: ",int(A)," A szám törtrésze: ",e)

# Feladat_10

'''

'''

A = float(input("szám:"))

print("%.2f" % (A))                                          # Feladat_11

'''

'''

A = float(input("szám1:"))
B = float(input("szám2:"))

a = math.pow(A,2) 
b = math.pow(B,2) 

x = math.sqrt(a + b)           
print(x,"távolságra vannak egymástól")                  # Feladat_12


# https://matekarcok.hu/a-koordinata-rendszerben-adott-ket-pont-tavolsaganak-a-meghatarozasa/

'''

'''

A = input("Név:")
B = float(input("Testtömeg:"))
C = float(input("Magasság(m):"))

C = C * 100
C = math.pow(C,2) 
T = B / C * 10000

print(A,"testtömeg-index értéke",T)                       # Feladat_13

if 20<=T<=25:
    print("Normál súly")
elif 25<T<=30:
    print("túlsúly")
elif 30<T<=35:
    print("I. fokú elhízás")
elif 35<T<=40:
    print("II. fokú elhízás")
elif 40<T<=100:
    print("III. fokú elhízás")
else:
    print("Gurulj tova!")


# https://www.webbeteg.hu/calc_testsuly

'''

'''

a = int(input("átlagos havi villanyszámlája:"))

e = a * 12    
f = a / 39    
h = f * 0.85 / 1000 * math.pow(10,4) / 310  
i = h * h




print("Éves: %d \nÉves KWh: %.1f \nnapelemek száma:%.1f \nmin méret: %.1f nm2" % (e,f,h,i))                  # Feladat_14

'''

'''

a = int(input("ingatlan ár:"))

b = a * 0.0275
c = a * 0.015 
d = a * 0.04
e = 40000
f = 6600
g = a + b + c + d + e + f                                    # Feladat_15

print("ingatlanügynök: %d \nügyvéd: %d \ningatlan illeték: %d \nenergetikai tanúsítvány: %d \n Tulajdoni lap: %d \n végösszeg: %d " % (b,c,d,e,f,g))

'''

