sentence = 'There once lived a bee in a house by the sea.'
position = 0
while position < len(sentence)-10:
    index = position
    while index < position+10:
        print(sentence[index], end='')
        index += 1
    print()
    position += 1
#A tu już nie rozumiem :(
# position zaczyna od 0 potem zrobił, że index to position czyli 0  i tu zaczynam nie rozumieć
# while 0 jest mniejsze niż 0 +10 ???????
# print (sentence[index], end='')  napisz zdanie zaczynając od 0 i zakończ na '' (nie wiem co znaczy end='')
# wchodzimy w matematyczne rzeczy i ja przestaje to rozumieć :(
