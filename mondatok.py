import random
def nevelo(szo):
    mgh= "aáeéiíoóöőuúüű"
    s="A"
    if szo[0] in mgh:
        s="Az"
    return s

def jelzo():
    szinek= ["piros", "fehér", "zöld"]
    return szinek[random.randint(0,2)]
    #return random.choice(szinek)    

i=0
valasz="i"
while valasz == "i":
    szo = input("Kérek egy főnevet: ")
    print(f"{nevelo(szo)} {szo} {jelzo()}")
    i+=1
    if i>1:
        valasz=input("Szeretne újabb főnevet megadni? i/n")
