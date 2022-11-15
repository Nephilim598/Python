class Tanc:
    def __init__(self,tanc,lnev,fnev) -> None:
        self.tanc=tanc
        self.lany=lnev
        self.fiu=fnev
    def __str__(self) -> str:         # ezzek működik a print(t2)
        return f"{self.lany} táncol {self.fiu} nevű táncossal {self.tanc} táncot"

tancok=[]
def beolvas():
    f= open("tancrend.txt", encoding="UTF8")
    print("asd")
    while True:
        tancx=f.readline().strip()  # a strippel a szólözöket CB-t vágjuk le
        if tancx:
            lany=f.readline().strip()
            fiu=f.readline().strip()
            tancok.append(Tanc(tancx,lany,fiu))
        else:
            break


def kiir(lista):
    for i in lista:
        print(i)

def f2():
    print("Az első tánc",tancok[0].tanc)
    print("Az utolsó tánc",tancok[len(tancok)-1].tanc)
    print("Az utolsó tánc",tancok[-1].tanc)

def f3():
    counter=0
    for i in tancok:
        if i.tanc=="samba":
            counter+=1
    return counter


def f4():
    for i in tancok:
        if i.lany =="Vilma":
            print(i.tanc)

def f5():
    t=input("melyik táncra vagy kíváncsi?")
    counter=0
    for i in tancok:
        if i.tanc==t and i.lany=="Vilma":
            print(f"{i.tanc} bemutatóján Vilma párja {i.fiu} volt ")
            counter=1
    if counter==0:
        print(f"Vilma nem táncolt {t}")
        

def f8(): # melyik táncot hányszor adták elő   / dictionary gyak
    global db
    db={}
    for i in tancok:
        if i.tanc in db.keys():
            db[i.tanc]+=1
        else:
            db[i.tanc]=1
    print(db)
    for i in db.keys():
        print(i,db[i])







def main():
    beolvas()
    #kiir(tancok)
    #print("__________________")
    #f2()
    #print("__________________")
    #print(f3(),"samba van a listában")
    #print("__________________")
    #print(f"{f3()}samba van a listában")
    #print("__________________")
    #print(f4())
    #print("__________________")
    #f5()
    f8()












main()

"""
t1=Tanc("rumba","Ági","Béla")
print(t1.fiu)
t2=Tanc("Tangó","Juanita","Carlos")
print(t2.tanc)
print(t1)
print(t2)
"""

























