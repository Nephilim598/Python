

class Tanar:
    nev=""
    targy=""
    oszt=""
    oraszam=0



def beolvas():
    global Tanarok
    Tanarok=[]
    f=open(r"C:\Users\Diák\Desktop\OSZTÁLY\S13\Fanni\Python\beosztas.txt", encoding="UTF8")
    while True:
        sor= f.readline().strip()
        if not sor:
            break
        else:
            ember=Tanar()
            ember.nev=sor
            ember.targy=f.readline().strip()
            ember.oszt=f.readline().strip()
            ember.oraszam=int(f.readline().strip())
            Tanarok.append(ember)
    f.close()


def f1():
    print(len(Tanarok))

def f2():
    osszesen=0
    for i in Tanarok:
        osszesen+=i.oraszam
    return osszesen

def f3():
    osszesen=0
    tanarnev=input("add meg a tanár nevét: ")
    for i in Tanarok:
        if i.nev == tanarnev:
            osszesen+=i.oraszam
    return osszesen



def main():
    beolvas()
    f1()
    print(f2())
    print(f3())
    print(Tanarok[0].nev)

main()