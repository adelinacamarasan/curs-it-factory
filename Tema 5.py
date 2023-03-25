'''Pentru toate exercitiile
Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
Daca functia are return, printati raspunsul
ex 1. Functie care sa calculeze si sa returneze suma a 2 numere
'''
print('exercitiul 1')
def suma_mea(x, y):
    suma = x + y
    return suma
print(suma_mea(5, 5))
print(suma_mea(3, 2))

print('exercitiul 2')
#ex 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
def este_nr_par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False
print(este_nr_par(9))
print(este_nr_par(8))

print('exercitiul 3')
#ex 3. Functie care returneaza numarul total de caractere din numele tau complet.(nume, prenume, nume_mijlociu)

def numar_total_caractere(*numeComplet):
    numar_caractere = 0
    for nume in numeComplet:
        numar_caractere += len(nume)
    return numar_caractere

suma = numar_total_caractere('Camarasan', 'Adelina', 'Delia')
print(suma)
suma = numar_total_caractere('Camarasan', 'Vlad')
print(suma)

print('exercitiul 4')
# ex 4. Functie care returneaza aria dreptunghiului.

def aria_dreptunghiului(lungime, latime):
    aria = lungime * latime
    print("aria_dreptunghiului: %.2f" %aria)
aria_dreptunghiului(5, 4)
aria_dreptunghiului(2, 4)

print('exercitiul 5')
#ex 5. Functie care returneaza aria cercului

def ariaCercului(r):
    PI = 3.14159265359
    return PI * (r * r);
print("Aria cercului este %.6f" % ariaCercului(5));

print('exercitiul 6')
#ex 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu
def exista_caracter(string, char):
    for caracter in string:
        if caracter == char:
            return True
    return False

rezultatul1 = exista_caracter('zebrele sunt frumoase','z')
print(rezultatul1)
rezultatul2 = exista_caracter('acadeaua este roz','i')
print(rezultatul2)

print('exercitiul 7')
'''ex 7. Functie fara return, primeste un string si printeaza pe ecran:
Nr de caractere lower case este x
Nr de caractere upper case exte y 
'''
def string_test(string):
    numar_caractere = {"UPPER_CASE": 0,
                       "LOWER_CASE": 0}
    for caracter in string:
        if caracter.isupper():
           numar_caractere["UPPER_CASE"] += 1
        elif caracter.islower():
           numar_caractere["LOWER_CASE"] += 1
        else:
           pass
    print("Original String : ", string)
    print("Nr de caractere Upper case este : ", numar_caractere["UPPER_CASE"])
    print("Nr de caractere Lower case este : ", numar_caractere["LOWER_CASE"])

string_test('Ce faci, Adelina?')

print('exercitiul 8')
'''ex 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive'''
# Function to print even numbers in a list

def numerePozitive(numere):
    lista_numere_pozitive = []
    for numar in numere:
        if numar > 0:
            lista_numere_pozitive.append(numar)
    return lista_numere_pozitive

list1 = [-2, -3, -4, 5, 6]
print(numerePozitive(list1))

list2 = [-2, -345, -567, 89, 9999, 0]
print(numerePozitive(list2))

print('exercitiul 9')
'''ex 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale. 
'''
def douaNumere(a, b):
    if a > b:
        print(f"{a} este mai mare decat {b}")
    elif b > a:
        print(f"{b} este mai mare decat {a}")
    else:
        print(f"{a} si {b} sunt egale")

douaNumere(2,10)
douaNumere(8, 6)

print('exercitiul 10')
'''ex 10. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
'''
def adaugareSetNumere(numar, SetNumere):
    if numar in SetNumere:
        print(f"N-am adaugat numarul {numar} , deoarece acesta exista deja.")
        return True
    else:
        SetNumere.add(numar)
        print(f"Am adaugat numarul {numar} la set.")
        return False

numere = {10, 20, 30}
adaugat = adaugareSetNumere(10, numere)
print(adaugat)

adaugat = adaugareSetNumere(40,numere)
print(adaugat)