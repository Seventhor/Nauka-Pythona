pyramid_size = int (input ("Give me a Pyramid size: "))
i = 1
while i <= pyramid_size:
    spacing = pyramid_size - i
    print(" " * spacing + "#" * (i*2))
    i += 1
#If statements i nesting było super i wszystko łatwe ale tego znowu nie rozumiem :(
#Chyba nie rozumiem matematyki w pythonie
#Linijki 1, 2, 3 rozumiem bez problemu, 4 również ale 5 nie rozumiem za grosz "spacja" razy (wielkość piramidy - 1) dodać # razy (1 razy 2)
