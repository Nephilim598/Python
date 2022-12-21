while True:
    elso = float(input("Kérem az első negativ számot: "))
    if elso<0:
        break
    else:
        print("az első  szám nem negativ!")

while True:
    masodik = float(input("Kérem a masodik negativ számot: "))
    if masodik<0:
        break
    else: 
        print("A második szám nem negativ!")
if elso> masodik: 
    print("Az első szám nagyobb")
elif elso<masodik:
    print("A második szám nagyobb")
else: 
    print("A két szám egyforma")



