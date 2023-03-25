print('exercitiul 1')
''''ex 1.Clasa Cerc.Atribute: raza, culoare
Constructor pt ambele atribute
Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria 
diametru() 
circumferinta()
'''
class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Raza este {self.raza} si culoarea este {self.culoare}')

    def aria(self):
        print(f'Aria cercului este {3.14 * 5}')

    def diametrul(self):
        print(f'Diamentrul cercului este {2 * 5}.')

    def circumferinta(self):
        print(f'Circumferinta cercului este {2 * 3.14 * 5}.')

cerc1 = Cerc(5, 'verde')
cerc1.descrie_cerc()
cerc1.aria()
cerc1.diametrul()
cerc1.circumferinta()

cerc2 = Cerc(3, 'mov')
cerc2.descrie_cerc()
cerc2.aria()
cerc2.diametrul()
cerc2.circumferinta()

print('exercitiul 2')
'''ex 2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pt toate atributele
Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare 
si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''
class Dreptunghi:
    def __init__(self, lungime, latime, culoarea):
        self.lungime = lungime
        self.latime = latime
        self.culoarea = culoarea

    def descrie_dreptunghi(self):
        print(f'Dreptunghiul are lungimea {self.lungime}, latimea {self.latime} si culoarea {self.culoarea}.')

    def aria_dreptunghiului(self):
        print(f'Aria dreptunghiului este {self.lungime * self.latime}.')

    def perimetrul_dreptunghiului(self):
        print(f'Perimetrul dreptunghiului este {2 * self.lungime * self.latime}.')

#perimetrul=2*(Lxl)

dreptunghi1 = Dreptunghi(8, 4, 'roz')
dreptunghi1.descrie_dreptunghi()
dreptunghi1.aria_dreptunghiului()
dreptunghi1.perimetrul_dreptunghiului()

dreptunghi2 = Dreptunghi(10, 5, 'albastru')
dreptunghi2.descrie_dreptunghi()
dreptunghi2.aria_dreptunghiului()
dreptunghi2.perimetrul_dreptunghiului()

print('exercitiul 3')
'''ex 3.
Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''
class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere_angajat(self):
        print(f'Numele angajatului este {self.nume}, prenumele angajatului este {self.prenume} si are salariul de {self.salariu} lei.')

    def salariu_lunar(self):
        print(f'Are salariul lunar de {self.salariu} lei.')

    def salariu_anual(self):
        print(f'Are salariul anual de {12 * self.salariu} lei.')

    def marire_salariu(self, procent):
        print(f'Angajatului i se va mari salariul cu {procent} % adica cu {procent/100 * self.salariu} lei.')


angajat1 = Angajat('Cherestes', 'Andreea', 5500)
angajat1.descriere_angajat()
angajat1.salariu_lunar()
angajat1.salariu_anual()
angajat1.marire_salariu(10)

angajat2 = Angajat('Ifrim', 'Mihaela', 6500)
angajat2.descriere_angajat()
angajat2.salariu_lunar()
angajat2.salariu_anual()
angajat2.marire_salariu(5)

print('exercitiul 4')
'''ex 4. Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate
Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''
class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self, suma):
        self.sold = self.sold + suma
        print(f'Contul a fost debitat cu {suma} lei.')
        print(f'Contul are {self.sold} lei.')

    def creditare_cont(self, suma):
            self.sold = self.sold - suma
            print(f'Contul a fost creditat cu {suma} lei.')
            print(f'Contul are {self.sold} lei.')

cont1 = Cont('R012BTRLRONCRT005566', 'Cherestes Andreea', 8000)
cont1.afisare_sold()
cont1.debitare_cont(200)
cont1.creditare_cont(400)

cont2 = Cont('R012BTRLRONCRT889933', 'Ifrim Mihaela', 9000)
cont2.afisare_sold()
cont2.debitare_cont(1000)
cont2.creditare_cont(5000)

print('BONUS-exercitiul 5')
'''ex 5.Clasa Factura
Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, 
cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti
Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total 
Telefon |      7       |       700       | 49000     
'''
class Factura:
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret = pret

    def schimba_nume_produs(self, nume):
        self.nume = nume

    def genereaza_factura(self):
        print('Produs  | cantitate | pret bucata | Total ')
        print(f'{self.nume_produs} | {self.cantitate}         | {self.pret_buc}         | {self.cantitate * self.pret_buc}')

factura1 = Factura(1, 'telefon', 3, 100)
factura1.genereaza_factura()



