text = input ("Napisz jakieś zdanie: ")
duze_litery = 0
male_litery = 0
for index in range (0, len(text)):
    char = text[index]
    if char.isupper():
        duze_litery += 1
    elif char.islower():
        male_litery += 1
print ("Ilość dużych liter w twoim zdaniu:" + str(duze_litery))
print ("Ilość małych liter w twoim zdaniu:" + str(male_litery))
