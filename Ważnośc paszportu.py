obecny_rok = int ( input ('Ktory mamy rok?: '))
rok_otrzymania = int ( input ('W ktorym roku otrzymales paszport?: '))
if rok_otrzymania + 10 < obecny_rok:
    print ('Powinienes zrobic nowy paszport!')
if rok_otrzymania + 10 == obecny_rok:
    print ('Konczy sie termin waznosci twojego paszportu!')
if rok_otrzymania + 10 > obecny_rok:
    print ('Twoj paszport jest aktualny!')
