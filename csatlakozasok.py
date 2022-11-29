import datetime

# feladat: http://infojegyzet.hu/vizsgafeladatok/okj-programozas/rendszeruzemelteto-191008/


class csatlakozasok:
    def __init__(self,orszag,datum) -> None:
        self.orszag= orszag
        self.datum= datum

    def __str__(self):
        return f"{self.orszag} {self.datum}"



lista = []

def beolvas():
    f= open("csatlakozas.txt", encoding="UTF8")
    for sor in f:
        reszek=sor.strip().split(";")
        orszag=reszek[0]
        datum= datetime.datetime.strptime(reszek[1],"%Y.%m.%d")
        obj= csatlakozasok(orszag, datum)
        lista.append(obj)


    for item in lista:
        print(item)


def f3():
    print(f"3. feladat: Eu tagállamok száma 2018-ban: {len(lista)}")


def f4(ev):
    db=0
    for item in lista:
        if item.datum.year == ev:
            db+=1
    print(f"4.feladat: {ev}-ben {db} csatlakozott")


def f5(orszag):
    i=0
    while lista[i].orszag != orszag:
        i+=1
    print(f"5.feladat: {orszag} csat date: {lista[i].datum}")


def f6():
    i=0
    while i<len(lista) and lista[i].datum.month == 5:
        i+=1
    if i<len(lista):
        print(f"6.feladat: volt májusban csatlakozás")
    else:
        print(f"6. feladat: Nem volt májusban csatlakozás")



def f7():
    max=lista[0]
    for item in lista:
        if max.datum < item.datum:
            max = item
    print(f"7. feladat: legkésőbb csat {max.orszag}")



def f8():
    # szótár adatszerkezet (dictionary)
    # kulcs ami alapján a statisztikát készítem
    #érték: adott évben hány csatlakozás volt

    stat={}
    for item in lista:
        kulcs= item.datum.year
        if kulcs not in stat: # ha még  kulcs nem szerepel a statisztikámban
            stat[kulcs]=0 # létrehozom a 0 kezdőértékkel
        stat[kulcs]+=1 # stat[kulcs] a kulcshoz tartozó értéket adja vissza

    for item in stat:
        print(f"{item}: {stat[item]}")





def main():
    beolvas()
    f3()
    f4(2007)
    f5("Magyarország")
    f6()
    f7()
    f8()


main()














