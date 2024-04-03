szerokosc = input("Flag szerokosc:\n")
szerokosc = int(szerokosc)
wysokosc = input("Flag wysokosc:\n")
wysokosc = int(wysokosc)

pol_szerokosc = int (szerokosc / 2)
pol_wysokosc = int (wysokosc / 2)

gora = '#' * pol_szerokosc + '-' * pol_szerokosc + '\n'
dol = '-' * szerokosc + '\n'

print (gora * pol_wysokosc, end='')
print (dol * pol_wysokosc, end='')


