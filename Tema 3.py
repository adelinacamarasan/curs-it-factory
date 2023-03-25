'''TEMA 3,
ex 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a. Afiseaz-o
b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
varianta actuala (inversata)
c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
varianta inițială
Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa
suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face
suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își
găsesc utilitatea în funcție de ce ne dorim in acel moment.'''
from turtle import update

lista_note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(lista_note_muzicale)
print({lista_note_muzicale[0]})
print({lista_note_muzicale[3]})
lista_note_muzicale = lista_note_muzicale[::-1]
print(lista_note_muzicale)
print({lista_note_muzicale[3]})

#EX 2-Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.

lista_note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']

nota1 = 'do'
nota = lista_note_muzicale.count(nota1)
print(f'count of {nota1}:', nota)

#EX 3-Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.

listA = [3, 1, 0, 2]
listB = [6, 5, 4]
listC = listA + listB
print(listC)

#EX 4-Sorteaza si afiseaza lista generata la exercitiul anterior.
#Sterge numarul 0 din lista folosind o functie si apoi afiseaza din nou lista

listC = listA + listB
listC.sort()
print(listC)

listC.remove(0)
print('Updated list', listC)

#EX 5-Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
#- Lista este goala (IF)
#- Lista nu este goala (ELSE)

listC = [listA + listB]
if listC:
    print('Lista nu este goala')
else:
    print('Lista este goala')

#EX 6-Foloseste o functie care sa goleasca lista de la exercitiul 3

listC.clear()
print(listC)

#EX 7-Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul.Acum ar trebui sa se afiseze ca lista e goala.
if listC:
    print('Lista nu este goala')
else:
    print('Lista este goala')

#EX 8-Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa afisezi Elevii (cheile)
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
print(dict1.keys())

#EX 9-Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor.Ex: ‘Ana a luat nota {x}’.
#Doar nota o vei lua folosindu-te de cheie

dict2 = {
    'Ana': 1,
    'Gigel': 10,
    'Dorel': 5
}
print(f'Ana a luat nota {dict2["Ana"]}')
print(f'Gigel a luat nota {dict2["Gigel"]}')
print(f'Dorel a luat nota {dict2["Dorel"]}')

#EX 10-Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.- Modifica nota lui Dorel in 6
# - Printeaza nota lui dupa modificare

dict3 ={
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
print('Ana = ', dict3['Ana'])
print('Gigel = ', dict3['Gigel'])
print('Dorel = ', dict3['Dorel'])

dict3.update({'Dorel': 6})
print('Dorel = ', dict3['Dorel'])

'''EX 11-Imagineaza-ti ca Gigel se transfera din clasa.- Cauta o functie care sa il stearga
Vine un coleg nou. Adaugati-l in lista pe Ionica, cu nota 9. Printati dictionarul cu noii elevi'''
print('ex 4 *********')

dict4 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}

dict4.pop('Gigel')
print(dict4)

dict4['Ionica'] = '9'
print(dict4)

'''#EX 12-Ai urmatoarele seturi:
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
- Incearca sa adaugi in setul zile_sapt ziua de ‘luni’ si observa ce se intampla.
- Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.'''

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.add('luni')
print(zile_sapt)

'''EX 13-.Foloseste un if si verifica daca:
- Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
regasesc intre elementele din setul zile_sapt)
- Weekend nu este un subset al zilelor din sapt
Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
punct de mai sus va fi un boolean'''

zile_sapt1 = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend1 = {'sambata', 'duminica'}

print(weekend1.issubset(zile_sapt))

if weekend1.issubset(zile_sapt1):
    flag1 = 1

if all(zi in zile_sapt1 for zi in weekend1):
    flag2 = 1

# printing result
if (flag1):
    print("Yes, list is subset of other.")
else:
    print("No, list is not subset of other.")

# printing result
if (flag2):
    print("Yes, list is subset of other.")
else:
    print("No, list is not subset of other.")

#EX 14-Afiseaza diferentele dintre aceste 2 seturi(adica elementele care sunt in zile_sapt si nu sunt in weekend si invers)

zile_sapt2 = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend2 = {'sambata', 'duminica', 'extra'}

diferente_zile_sapt = zile_sapt2.difference(weekend2)
diferente_weekend = weekend2.difference(zile_sapt2)

print(f'diferente_zile_sapt  {diferente_zile_sapt}')
print(f'diferente_weekend {diferente_weekend}')

diferente_final = diferente_zile_sapt
diferente_final.update(diferente_weekend)

print(f'diferente_final  {diferente_final}')

#EX 15-Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in ambele seturi).
# Hint: Va puteti folosi de o functie.

zile_sapt3 = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend3 = {'sambata', 'duminica', 'extra'}

intersectare_liste = zile_sapt3.intersection(weekend3)

print(intersectare_liste)

