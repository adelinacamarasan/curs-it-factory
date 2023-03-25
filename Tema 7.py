'''ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
'''
from abc import abstractmethod
print('ex 1')
class FormaGeometrica:
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def description(self):
        print(f'Cel mai probabil am colturi')


forma = FormaGeometrica()
forma.description()

'''INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)
'''

class Patrat(FormaGeometrica):
    def __init__(self):
        self.latura = 0

    def setLatura(self, latura):
        self.latura = latura
        print(f'Valoarea setata a laturei este {self.latura}')

    def getLatura(self):
        # print(f'Valoarea luata a laturei este {self.latura}')
        return self.latura

    def deleteLatura(self):
        self.latura = 0
        print(f'Valoarea laturei a fost stearsa si este {self.latura}')

    def aria(self):
        aria = self.latura * self.latura
        print(f'Aria patratului este {aria}')
        return aria


patrat = Patrat()
patrat.getLatura()
patrat.setLatura(5)
print(patrat.getLatura() + patrat.getLatura())
patrat.description()

patrat1 = Patrat()
patrat1.setLatura(5)

print(patrat.aria() + patrat1.aria())


'''Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)

POLYMORPHISM 
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
'''

class Cerc(FormaGeometrica):
    def __init__(self):
        self.raza = 0

    def setRaza(self, raza):
        self.raza = raza
        print(f'Valoarea setata a razei este {self.raza}')

    def getRaza(self):
        # print(f'Valoarea luata a razei este {self.raza}')
        return self.raza

    def deleteRaza(self):
        self.raza = 0
        print(f'Valoarea razei a fost stearsa si este {self.raza}')

    def aria(self):
        return self.PI * self.raza * self.raza

cerc = Cerc()
cerc.setRaza(5)
cerc.getRaza()
print(f'Aria cercului este {cerc.aria()}')