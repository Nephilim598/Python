from hiresno import Hiresno
from operator import attrgetter

def d_feladat():
    f = open("hires.txt", encoding="UTF-8")
    global lista
    lista = []
    f.readline()
    for sor in f:
        adatok = sor.rstrip().split(";")
        nev = adatok[0]
        nemzetiseg = adatok[1]
        foglalkozas = adatok[2]
        obj = Hiresno(nev, nemzetiseg, foglalkozas)
        lista.append(obj)
    f.close()

def lista_kiir():
    print(*lista, sep="\n")

def f_feladat():
    return len(lista)

def g_feladat():
    db = 0
    for elem in lista:
        if elem.nemzetiseg == "amerikai":
            db += 1
    return db

def h_feladat(nemzetiseg):
    i = 0
    while i < len(lista) and lista[i].nemzetiseg != nemzetiseg:
        i += 1
    if i < len(lista):
        return lista[i].nev
    else:
        return None

def j_feladat():
    f = open("fizikusok.txt", "w", encoding="UTF-8")
    l = sorted(lista, key=attrgetter('nev'))
    for elem in l:
        if "fizikus" in elem.foglalkozas:
            print(f"{elem.nev}: {elem.nemzetiseg}", file=f)
            # f.write(f"{elem.nev}: {elem.nemzetiseg}\n")



def main():
    d_feladat()
    lista_kiir()
    print(f"\nf) feladat:\n\tA híres nők száma: {f_feladat()}")
    print(f"\ng) feladat:\n\tAz amerikai hírességek száma: {g_feladat()} fő ")
    # h) feladat: Nincs a listában horváth nemzetiségű híresség!
    #  i) feladat: Van a listában szerb nemzetiségű híresség: Mileva Marić

    ho = h_feladat("horváth")
    if ho != None:
        print(f"\ni) feladat:\n\tVan a listában horváth nemzetiségű híresség: {ho}")
    else:
        print("\ni) feladat:\n\tNincs a listában horváth nemzetiségű híresség!")

    sze = h_feladat("szerb")
    if sze != None:
        print(f"\ni) feladat:\n\tVan a listában szerb nemzetiségű híresség: {sze}")
    else:
        print("\ni) feladat:\n\tNincs a listában szerb nemzetiségű híresség!")

    j_feladat()
    print("\nj) feladat:\n\tA fizikusok.txt állomány létrejött.") 
    
main()