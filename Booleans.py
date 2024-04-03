niebo_jest_niebieskie = True
jedzenie_jest_kiepskie = False
print (niebo_jest_niebieskie, jedzenie_jest_kiepskie)
print ('--------------------------------------------------')
print('Dodatkowy print')

koszt_domu = int (input ('Ile kosztuje dom?: '))
dostepna_kasa = int (input ('Ile masz teraz kasy?: '))
down_payment = koszt_domu * 0.2
if dostepna_kasa >= down_payment:
    print ('stać cie na kupno domu')
