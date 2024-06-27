

def rysuj_glowe(wlosy, oko):

    print(wlosy * 12)
    print(wlosy + '|        |' + wlosy)
    print(wlosy + '|  ' + oko + '  ' + oko + '  |' + wlosy)
    print(' |   /\   |' )
    print(' |        |' )
    print(' \  \'--\'  /')
    print('   ------')

def rysuj_tulow(wysokosc, ramie):

    print('     XX')
    print('#' + (ramie*4) + 'XX' + (ramie*4) + '#')
    print('    XXXX\n' * wysokosc, end='')

def rysuj_nogi(wysokosc, but):

    print('    ====')
    print('   ||  ||\n' * wysokosc, end='')
    print(' ' + but + '  ' + odwroc_but(but))

def odwroc_but(but):


    return but[::-1]

def main():
    print('Witaj w narzędziu do tworzenia postaci!')
    wysokosc = int(input('Całkowita wysokość postaci: '))
    wlosy = input('Znak dla włosów: ')
    oko = input('Znak dla oczu: ')
    ramie = input('Znak dla ramion: ')
    but = input('Czteroznakowy string dla butów: ')
    segment = (wysokosc - 11) // 2

    print()
    rysuj_glowe(wlosy, oko)
    rysuj_tulow(segment, ramie)
    rysuj_nogi(segment, but)

main()
