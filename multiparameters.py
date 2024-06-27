def oblicz_podatek(dochod, ulgi):
    netto = dochod - ulgi
    if netto < 50000:
        return netto * 0.15
    elif netto < 100000:
        return netto * 0.20
    return netto * 0.25

def oblicz_miesieczna_rate(kwota, lata, oprocentowanie):
    miesieczne_oprocentowanie = oprocentowanie / 12
    miesiace = lata * 12
    gora = kwota * (miesieczne_oprocentowanie * (1 + miesieczne_oprocentowanie)**miesiace)
    miesieczna_rata = gora / ((1 + miesieczne_oprocentowanie)**miesiace - 1)
    return miesieczna_rata

def main():
    pensja         = int(input('Ile zarobiłeś w tym roku? '))
    ulgi_uzytkownika = int(input('Jakie masz ulgi podatkowe? '))
    hipoteka       = int(input('Ile wynosi Twoja hipoteka? '))
    lata           = int(input('Na ile lat masz hipotekę? '))
    oprocentowanie = float(input('Jakie jest oprocentowanie Twojej hipoteki? '))

    wynik = oblicz_podatek(pensja, ulgi_uzytkownika)
    print('Jesteś winien ' + str(wynik) + ' zł w podatkach.')

    wynik = oblicz_miesieczna_rate(hipoteka, lata, oprocentowanie)
    print('Twoja miesięczna rata hipoteczna wynosi ' + str(wynik) + ' zł.')

main()
