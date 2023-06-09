
print('Exercitiul 1')
'''TEMA 4
ex 1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

print('for')
for i in range(len(masini)):
    print('Masina mea preferata este ' + masini[i])

print('for each')
for masina in masini:
    print('Masina mea preferata este ' + masina)

print('while')
i = 0
while i < len(masini):
    print('Masina mea preferata este ' + masini[i])
    i += 1
print('Exercitiul 2')
'''ex 2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrise cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

for i in range(len(masini)):
    if i == 0 or i == len(masini) - 1:
       continue
    else:
        masini[i] = masini[i].upper()
print(masini)


print('Exercitiul 3')
'''ex 3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes. Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Mercedes':
        print(f'Am găsit mașina {masina} dorită de dvs')
        break
    else:
        print(f'Am găsit mașina {masina}. Mai căutam')

print('Exercitiul 4')
'''ex 4. Aceeași listă;
Vine un cumpărător bogat, dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
        continue
    print(f'S-ar putea să vă placă mașina {masina}.')

print('Exercitiul 5')
'''5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

● Printează Modele vechi: x.
● Modele noi: x.'''

masini_vechi = []
print(masini_vechi)

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for i in range(len(masini)):
    if masini[i] == 'Lăstun' or masini[i] == 'Trabant':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'

print("Modele vechi: ", masini_vechi)
print("Modele noi: ", masini)

print('Exercitiul 6')
'''ex 6. Vine un client cu un buget de 15000 euro.
Prezintă doar mașinile care se încadrează în acest buget.
Itereaza prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină x Lastun. Iterează prin listă.
'''
preturi_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

buget = 15000
for masina, pret in preturi_masini.items():
    if pret <= buget:
        print(f"Pentru un buget de sub {buget} euro, puteți alege mașina: {masina} ")

print('Exercitiul 7')
'''ex 7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea. Afișează de câte ori apare 3 (nu ai voie să folosești count).'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

cifra_3 = 0
for numar in numere:
    if numar == 3:
        cifra_3 += 1

print("In lista, cifra 3 apare de atatea ori :", cifra_3)

print('Exercitiul 8')
'''ex 8. Aceeași listă:
Iterează prin ea.Calculează și afișează suma numerelor (nu ai voie să folosești sum).'''

total = 0
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for element in range(0, len(numere)):
    total = total + numere[element]
print("Suma tuturor numerelor din lista este: ", total)

print('Exercitiul 9')
'''ex 9. Aceeași listă:
● Iterează prin ea.
● Afișează cel mai mare număr (nu ai voie să folosești max).'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nrmaxim = 0
for nr in numere:
    if nr > nrmaxim:
        nrmaxim = nr
numere.sort()
print(f'nrmax {nrmaxim}')
print("Cel mai mare numar din lista este:", numere[-1])

print('Exercitiul 10')
'''ex 10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișează noua listă.'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if(numere[i] > 0):
        numere[i] = numere[i] - numere[i] - numere[i]
print(numere)



