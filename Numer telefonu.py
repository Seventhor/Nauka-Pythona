# Program do sprawdzania formatu numeru telefonu

phone = input('Wprowadź swój numer telefonu : ')

# Długość numeru (Z 48)
if len(phone) != 12:
    print('Nieprawidłowy numer telefonu!')
else:
    # Czy na 4 i 8 jest myślnik
    if phone[3] != '-' or phone[7] != '-':
        print('Nieprawidłowy numer telefonu!')
    else:
        # Sprawdza czy znaki to cyfry
        valid = True
        for i in range(12):
            if i != 3 and i != 7:
                if not phone[i].isdigit():
                    valid = False
                    break
        if valid:
            print('Prawidłowy numer telefonu!')
        else:
            print('Nieprawidłowy numer telefonu!')
