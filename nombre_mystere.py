import random

nombre_secret = random.randint(1, 10)

print("J'ai choisi un nombre entre 1 et 10.")

proposition = int(input("Devine le nombre : "))

if proposition == nombre_secret:
    print("Bravo !")
else:
    print("Perdu ! Le nombre était", nombre_secret)