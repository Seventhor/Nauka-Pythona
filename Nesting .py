głodny = input ("Jesteś głodny?: ")
if głodny == "Tak":
    ok = input ("Co powinieneś zjeść?: ")
    if ok == "pizza":
        print ("zamów se pizze")
    elif ok == "burger":
        print ("Zamów se burgera")
    elif ok == "Sałatka":
        print ("Głupi jesteś? chcesz marnować tyle kasy na pare liści sałaty z jakimis dodatkami?")
    else:
        print ("Zdecyduj sie a teraz lecimy dalej")
else:
    print ("To lecimy dalej")

pragnienie = input ("Chce ci sie pić?: ")
if pragnienie == "Tak":
    ok2 = input ("Co powineneś sie napić?: ")
    if ok2 == "cole":
        print ("jak masz cole to pij jak nie won do sklepu")
    elif ok2 == "wode":
        print ("Spoko pij wode")
    elif ok2 == "sok":
        print (" Jak masz sok to pij i pracujemy dalej jak nie idź do sklepu")
else:
    print ("parcuj dalej")
