def beolvasketlista():
    f=open(r"C:\Users\Diák\Desktop\OSZTÁLY\S13\Fanni\Python\emberek.txt",encoding="UTF8")
    global nevek
    global fizuk
    nevek=[]
    fizuk=[]
    for sor in f:
        nev=sor.split(";")[0]              # a split vág és tömböt hoz létre / listát                / a [0] a rekeszz a 0. rekesz
        nevek.append(nev)
        fizuk.append(int(sor.split(";")[1]))                      # itt nem rakjukkülön változóba hanem azonnal listába


def kiirketlista(lista):
    for i in lista:
        print(i)
        

def kiirketlista2(nevek,fizuk):
    for i in range(len(nevek)):
        print(f"név: {nevek[i]}, fizuk: {fizuk[i]}")


def filebair():
    f=open("fizetesek.txt", "w", encoding="UTF8")
    for i in range(len(nevek)):
        f.write(f"név: {nevek[i]}, fizuk: {fizuk[i]}\n")


def main():
    beolvasketlista()
    filebair()
   

main()