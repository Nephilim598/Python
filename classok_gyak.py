class Hires:
    def __init__(self,nev,szakma,nemzet) -> None:
        self.nev=nev
        self.szakma=szakma
        self.nemzet=nemzet

    def hogyan(self):
        if self.nemzet=="a":
            return "Ms"
        else:
            return "Frau"





def main():
    csajok=[]
    for i in range(3):
        nev=input("add meg a nevet")
        szakma=input("add meg a szakmát")
        nemzet=input("add meg a nemzetiségét")
        csajok.append(Hires(nev, szakma, nemzet))
    for i in csajok:
        print(i.hogyan(),i.nev,"egy híres", i.szakma)

main()






