import random

def wczytaj_pytania_i_odpowiedzi(nazwa_pliku):

    pytania_odpowiedzi = {}
    with open(nazwa_pliku, 'r') as plik:
        for linia in plik:
            pytanie, odpowiedz = linia.strip().split('|||')
            pytania_odpowiedzi[pytanie] = odpowiedz
    return pytania_odpowiedzi

def wybierz_losowe_pytanie(pytania_odpowiedzi):

    return random.choice(list(pytania_odpowiedzi.keys()))

def zadaj_pytanie(pytania_odpowiedzi):

    pytanie = wybierz_losowe_pytanie(pytania_odpowiedzi)
    odpowiedz = input(pytanie + " ")
    if odpowiedz.lower() == pytania_odpowiedzi[pytanie].lower():
        del pytania_odpowiedzi[pytanie]
        return True
    return False

def main():
    nazwa_pliku = input('Podaj nazwę pliku z pytaniami: ')
    liczba_pytan = int(input('Ile pytań ma zostać zadanych? '))
    pytania_odpowiedzi = wczytaj_pytania_i_odpowiedzi(nazwa_pliku)
    liczba_poprawnych_odpowiedzi = 0

    for _ in range(liczba_pytan):
        if zadaj_pytanie(pytania_odpowiedzi):
            liczba_poprawnych_odpowiedzi += 1

    print(f'Poprawnie odpowiedziałeś na {liczba_poprawnych_odpowiedzi} z {liczba_pytan} pytań.')
    procent_poprawnych = (liczba_poprawnych_odpowiedzi / liczba_pytan) * 100
    print(f'Twój wynik to: {procent_poprawnych:.2f}%')

main()
