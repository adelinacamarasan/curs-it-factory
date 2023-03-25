'''TEMA 2
EX 1: If else evalueaza niste conditii si in functie de rezultat,
in consola printeaza doar conditia care se indeplineste'''
#EX 2-Verifica si afiseaza daca x este numar natural sau nu:

x = -10
if x > 0:
    print('Este numar natural.')
else:
    print('Nu este numar natural.')

#EX 3-Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru:

x = -10
limita_zero = 3

if x > limita_zero:
    print(f'\'{x}\' este numar pozitiv')
elif x < limita_zero:
    print(f'\'{x}\' este numar negativ')
else:
    print(f'\'{x}\' este neutru')

#EX 4-Verifica si afiseaza daca x este intre -2 si 13

x = -10
limita_inferioara = -2
limita_superioara = 13
if x > limita_inferioara and x < limita_superioara:
    print(f'{x} este intre {limita_inferioara} si {limita_superioara}')
else:
    print(f'{x} nu este intre {limita_inferioara} si {limita_superioara}')

#EX 5-Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

x = -10
y = 5
diferenta_dintre_x_si_y = x - y
numar_verificare = 5

if diferenta_dintre_x_si_y < numar_verificare:
    print(f'diferenta dintre {x} si {y} este {diferenta_dintre_x_si_y} si este mai mic decat numarul de verificare {numar_verificare}')
else:
    print(f'diferenta dintre {x} si {y} este {diferenta_dintre_x_si_y} si este mai mare decat numarul de verificare {numar_verificare}')

#EX 6-Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

x = -10
if not (5 < x > 27):
    print('NU este intre 5 si 27')
else:
    print('x este intre 5 si 27')

#EX 7- x si y (int) Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare

x = -10
y = 5
if x == y:
    print(f'{x} si {y} sunt egale')
elif x > y:
    print(f'{x} este mai > decat {y}')
else:
    print(f'{y} este mai > decat {x}')

#EX 8- X, y, z - laturile unui triunghi.Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.

x = -10
y = -10
z = -10

if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
    print('Triunghiul este isoscel')
elif x == y == z:
    print('Tringhiul este echilateral')
else:
    print('Tringhiul este oarecare')

#EX 9-Citeste o litera de la tastatura.Verifica si afiseaza daca este vocala sau nu

litera = input(f'Introduceti o litera: ')
vocale = 'aeiou'
if litera.isalpha() and len(litera) == 1:
    if litera.lower() in vocale:
        print(f'{litera} Este vocala')
    else:
        print(f'{litera} Nu este vocala')
else:
    print(f'{litera} nu este litera sau contine mai multe caractere')

#EX 10-Transforma si printeaza notele din sistem romanesc in  >
#Peste 9 => A
#Peste 8 => B
#Peste 7 => C
#Peste 6 => D
#Peste 4 => E
#4 sau sub => F
nota = float(input("Care este nota primita? "))
if 9 < nota <= 10:
    nota = "A"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 8:
    nota = "B"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 7:
    nota = "C"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 6:
    nota = "D"
    print(f"Nota primita in sistemul american este {nota}")
elif nota > 4:
    nota = "E"
    print(f"Nota primita in sistemul american este {nota}")
elif 4 >= nota > 0:
    nota = "F"
    print(f"Nota primita este {nota}")
else:
    print('Nu ati introdus o nota de la 0 la 10.')



