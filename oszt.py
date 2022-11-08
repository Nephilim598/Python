
class Ember:
    nev=""
    fizu=0


def beolvas():
    f=open(r"C:\Users\Diák\Desktop\OSZTÁLY\S13\Fanni\Python\emberek.txt",encoding="UTF8")
    global emberek
    emberek=[]    
    # amúgy itt volt az alábbi ami rossz
    for sor in f:
        emb=Ember()  # emb változó az Ember sablonból készüljön lesz neve és fizetése  / ezt ide kell helyezni mert különben mindig felülírja az előzőt
        emb.nev=sor.split(";")[0]
        emb.fizu=int(sor.split(";")[1])
        print(emb.fizu,emb.nev)
        emberek.append(emb)

def kiir(emberek):
    for i in emberek:
        print(i.nev,i.fizu)

def osszes(emberek):
    osszeg=0
    for i in emberek:
        osszeg+=i.fizu
    return osszeg







beolvas()
#kiir(emberek)
print(osszes(emberek))




















