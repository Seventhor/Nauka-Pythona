earned = int (input ("Ile zarabisz? : "))
spent = int (input ("Ile wydajesz? : "))
if earned > spent:
    print ("Super, zarabiasz wiecej niż wydajesz.")
if earned == spent:
    print ("Kiepsko, nie jestes w stanie się utrzymać.")
if earned < spent:
    print ("Oj nie! zarabiasz mniej niż masz wydatków, może kolejna praca?")
