import math
class versenyzo:
    def __init__(self,helyezes,nev,orszag,nyeremeny) -> None:
        self.helyezes=helyezes
        self.nev=nev
        self.orszag=orszag
        self.nyeremeny=nyeremeny
    def __str__(self) -> str:
        return "Név:"+self.nev+", fizetése: "+str(self.fizetése*380)  # 380 mert forintba kell kiírni

versenyzok=[]

def beolvas():
    f=open("snooker.txt", encoding="UTF8")  # beolvasás
    f.readline() # ezzel átugorjuk az 1. sort
    for sor in f:  # végigmegyünk a txt-n
        temp=sor.strip().split(";")  # ;-ként szétvágjuk
        versenyzok.append(versenyzo(int(temp[0]),temp[1],temp[2],int(temp[3])))

def f3():
    print(f"A világlistán {len(versenyzok)} versenyző szerepel")   # az f azért kell hogy formázhassuk / a {} pedig h beírjuk a kódot

def f4():
    sum=0
    for item in versenyzok:
        sum+=item.nyeremeny
    print(round(sum/len(versenyzok),2))




def f5():
    maxsorszam=0    # 0 ha van és -1 ha nincs
    for i in range(len(versenyzok)):
        if versenyzok[i].orszag=="Kína" and versenyzok[i].nyeremeny>max:
            max=versenyzok[i].nyeremeny
            maxsorszam=i  # ez kell hogy a sorszám alapján kiírhassuk az adatait
    print(versenyzok[maxsorszam])  # ha nem használjuk a 2. def-et akkor (versenyzok[maxsorszam].nev)  stb írni kel mellé 




def f6(nemzetiseg):
    i = 0
    while i<len(versenyzok) and versenyzok[i].orszag != nemzetiseg:
        i+=1
    if i<len(versenyzok):
        return True
    else:
        return False


def f6_2():      # f6 könnyebben
    vanE=False
    for i in versenyzok:
        if item.orszag == "Norvégia":
            print("Van norvég")
            vanE = True
            break
    if not vanE:
        print("Nincs norvég")




def f7():
    # halmaz egy elem csak egyszer szerepelhet
    halmaz = set([])  # csak 1x kerül bele az adott dolog többx nem rakja bele
    for item in versenyzok:
        halmaz.add(item.orszag)
    for item in halmaz:
        print(f"{item}: {szamol(item)}")


def szamol(orszag):
    db= 0
    for item in versenyzok:
        if item.orszag == orszag:
            db+=1
    return db

def main():
    beolvas()
    f3()
    f4()
    f5()
    vanE= f6("Norvégia")
    print(vanE)
    f6_2()
    f7()


main()















