wzrost = int (input ("Wzrost w CM: "))
stan_konta = float (input ("Ile masz pieniedzy na koncie: "))


if wzrost >= 180:
    if stan_konta >= 10000.0:
            print (" Spoko bro każda na mazowieckiej twoja!")
if wzrost < 180:
    if stan_konta >= 10000.0:
            print (" Hmmm... Stawiaj drinki, afiszuj się kasą i miej dobrą nawijkę, powinno być git")
if wzrost >= 180:
    if stan_konta < 10000.0:
            print (" Na Mazowieckiej bedzie cieżko kolego")
if wzrost < 180:
    if stan_konta < 10000.0:
            print (" Nie ma bata ziomuś, nawet nie próbuj iść na Mazowiecką!")

