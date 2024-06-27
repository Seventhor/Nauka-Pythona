
PI = 3.14159
GRAVITY = 9.81

def oblicz_powierzchnie_kola(promien):

    return PI * promien * promien

def oblicz_predkosc_koncowa(czas):

    return GRAVITY * czas

def main():

    promien = float(input("Podaj promień koła: "))
    czas_spadania = float(input("Podaj czas spadania obiektu: "))


    powierzchnia = oblicz_powierzchnie_kola(promien)
    predkosc = oblicz_predkosc_koncowa(czas_spadania)


    print(f"Powierzchnia koła o promieniu {promien} wynosi: {powierzchnia}")
    print(f"Prędkość końcowa po {czas_spadania} sekundach wynosi: {predkosc}")


main()
