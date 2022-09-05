import random

kuutiot = int(input("Anna kuutioiden määrä"))
ennen_heittoa = 0

for kuutiot in range(kuutiot):
    heiton_jalkeen = random.randint(1, 6)
    ennen_heittoa += heiton_jalkeen
    print(heiton_jalkeen)

print(f"Noppien summa on: {ennen_heittoa}")

