import random

nr_cautat = int(input("Introdu nr: "))
nr = random.randint(0, 100)

nr_incercari = 10
while nr != nr_cautat and nr_incercari > 0:
    nr_incercari -= 1

    if nr_cautat < nr:
        print('Numarul este mai mare')
    elif nr_cautat > nr:
        print('Numarul este mai mic')1

    if nr_incercari > 0:
        nr_cautat = int(input("Introdu nr: "))

if nr == nr_cautat:
    print(f'Felicitări, ai ghicit numărul in {11-nr_incercari} incercari !')
else:
    print('Ai epuizat toate încercările. Numărul era', nr)
