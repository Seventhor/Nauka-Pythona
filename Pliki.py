def zapisz_do_pliku(nazwa_pliku, dane):

    with open(nazwa_pliku, 'w') as plik:
        plik.write(dane)
    print(f'Dane zostały zapisane do pliku {nazwa_pliku}.')

def odczytaj_z_pliku(nazwa_pliku):

    with open(nazwa_pliku, 'r') as plik:
        dane = plik.read()
    print(f'Dane odczytane z pliku {nazwa_pliku}:')
    return dane

def main():

    nazwa_pliku = 'przyklad.txt'
    dane_do_zapisania = 'To jest przykładowy tekst, który zapiszemy do pliku.'


    zapisz_do_pliku(nazwa_pliku, dane_do_zapisania)


    odczytane_dane = odczytaj_z_pliku(nazwa_pliku)
    print(odczytane_dane)

main()
