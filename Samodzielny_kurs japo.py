print ("Klasy jakie posiadamy to: Początkujący, Sredni, Średnio-Zaawansowany, Zaawansowany")
print ("Jeżeli dopiero rozpoczynasz Nauke wpisz 'nowy' ")
exp = input (" Jaki jest twój poziom Japońskiego?: ")

if exp == "Nowy":
    print (" Powinieneś zacząć od klasy dla Nowych ")
elif exp == "Początkujący":
    print (" Powinieneś zacząć od klasy dla Średnich ")
elif exp == "Średni":
    print (" Powinieneś zacząć od klasy Średnio Zaawansowanych")
elif exp == "Zaawansowany":
    print (" Powinieneś przenieść sie do bardziej zaawansowancyh klas")
else:
    print ("Nie posiadamy takiej klasy")
    print ("Sprawdź Czy dobrze wpisałeś klase")
