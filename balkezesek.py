import datetime 

# http://infojegyzet.hu/vizsgafeladatok/okj-programozas/szoftverfejleszto-200204/




class balkezes:
    def __init__(self,nev,elso,utolso,suly,magas) -> None:
        self.nev= nev
        self.elso= elso
        self.utolso=utolso
        self.suly=suly
        self.magas=magas

    def __str__(self):
        return f"{self.nev} {self.elso} {self.utolso} {self.suly} {self.magas}"

lista=[]


def beolvas():
    f = open("balkezesek.csv")
    f.readline()
    
    for sor in f:
        adatok = sor.strip().split(";")
        nev=adatok[0]
        elso = datetime.datetime.strptime(adatok[1], "%Y-%m-%d")
        utolso = datetime.datetime.strptime(adatok[2], "%Y-%m-%d")
        suly=adatok[3]
        magas=adatok[4]
        obj= balkezes(nev,elso,utolso,suly,magas)
        lista.append(obj)
    
    for item in lista:
        print(item)
    f.close()



def f3():
        print(f"3. feladat: {len(lista)}")

def f4():
    for i in lista:
        if i.utolso.year == 1999 and i.utolso.month == 10:
            print(f"{i.nev} {round((float(i.magas)*2.54),1)}  cm")

def f5():
    while (True): 
        global evszam
        evszam =int(input("Kérek egy 1990 és 1999 közötti évszámot pls: "))
        if(1990<= evszam and evszam <= 1999):
            break
        else: 
            print("Hibás adat, kérek egy 1990 és 1999 közötti évszámot!")


def f6():
    count = 0
    avg = 0
    for i in lista:
        if evszam == i.elso.year or evszam == i.utolso.year:
           avg  += i.suly
           count += 1
    print(avg/count)



def main():
    beolvas()
    f3()
    f4()
    f5()
    f6()

main()
































