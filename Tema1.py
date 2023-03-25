# o variabila string este un sir de caractere care se defineste in ghilimele

marca_sampon = 'Garnier'
print(f'Sampon marca {marca_sampon}.')

numar_sampon = 3
print(f'{numar_sampon} sampoane.')

numar_sampon_float = 3.474574
print(f'{numar_sampon_float} sampoane.')

is_spalat = True
print(f'{is_spalat} este spalat.')

for i in range(0, 20):
			print(i)

# 1. In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
# O variabila este o zona din memorie care tine date

# 2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# string, int, float, bool
# Valorile le alegeti voi dupa preferinte

# 3. Utilizati functia type pentru a verifica daca au tipul de date asteptat

marca_sampon = 'Garnier'
type(marca_sampon)
print(f'Sampon marca {marca_sampon}.')
print(f'Sampon marca {marca_sampon}.', type(marca_sampon))

numar_sampon = 3
print(f'{numar_sampon} sampoane.')
print(f'{numar_sampon} sampoane.', type(numar_sampon))

numar_sampon_float = 3.474574
print(f'{numar_sampon_float} sampoane.')
print(f'{numar_sampon_float} sampoane.', type(numar_sampon_float))

is_spalat = True
print(f'{is_spalat} este spalat.')
print(f'{is_spalat} este spalat.', type(is_spalat))


# 4. Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
# Verificati tipul acesteia
numar_rotunjit = 3.474574
print(f'{numar_rotunjit} nerotunjit.')
numar_rotunjit = round(numar_rotunjit)
print(f'{numar_rotunjit} rotunjit.')

#5.Folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
# Rezolvati nepotrivirile de tip prin ce modalitate doriti)
print(f'{marca_sampon} este un sampon.');
print(f'Mi-am cumparat {numar_sampon} bucati.');
print(f'{numar_sampon_float} este float.');
print(f'{is_spalat} =bun.');

# 6.Citeste de la tastatura numele
# citeste de la tastatura prenumele
# afiseaza 'Numele complet are x caractere'

nume_camarasan = input(f'Citeste de la tastatura numele: ')
prenume_adelina = input(f'Citeste de la tastatura prenumele: ')
numar_caractere_nume_complet = len(nume_camarasan) + len(prenume_adelina);
nume_complet = nume_camarasan + " " + prenume_adelina;
print(f'{nume_complet} are {numar_caractere_nume_complet} caractere')

'''7.Citeste de la tastatura lungimea
citeste de la tastatura latimea
afiseaza 'Aria dreptunghiului este x'
'''
lungime = int(input(f'Citeste de la tastatura lungimea dreptunghiului: '))
latime = int(input(f'Citeste de la tastatura latime dreptunghiului: '))
aria = lungime * latime
print(f'Aria dreptunghiului este {aria}');

'''8.Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
afisati de cate ori apare cuvantul 'the'
'''
# to count words in string
propozitie = 'coral is either the stupidest animal or the smartest rock'
lista_cuvinte = propozitie.split()
print(lista_cuvinte)
print(lista_cuvinte.count('the'))

#9.Acelasi string.Inlocuieste the cu THE peste tot.Printeaza rezultatul
propozitie = 'coral is either the stupidest animal or the smartest rock'
print(propozitie.replace('the', 'THE'))

#10.Acelasi string de mai sus.Folositi un assert ca sa verificati daca acest string contine doar numere.
propozitie = 'coral is either the stupidest animal or the smartest rock'

assert not propozitie.isdigit()
print('Contine numere.')

# assert propozitie.isdigit()
# print('Nu contine numere.')








