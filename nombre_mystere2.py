import random

nombre_secret = random.randint(1, 500)

tentatives = 0

print("=== JEU DU NOMBRE MYSTÈRE ===")
print("Je pense à un nombre entre 1 et 500.")
print("Essaye de le deviner !")

while True:
    proposition = int(input("Ton nombre : "))
    tentatives += 1

    if proposition < nombre_secret:
        print("Trop bas !")
    elif proposition > nombre_secret:
        print("Trop haut !")
    else:
        print()
        print("Bravo !")
        print("Tu as trouvé le nombre en", tentatives, "tentative(s).")
        break

# Sauvegarde du score
with open("scores.txt", "a") as fichier:
    fichier.write(str(tentatives) + "\n")

# Lecture des scores
with open("scores.txt", "r") as fichier:
    scores = []

    for ligne in fichier:
        scores.append(int(ligne.strip()))

scores.sort()

print()
print("=== CLASSEMENT DES MEILLEURS SCORES ===")

for i in range(min(5, len(scores))):
    print(f"{i+1}. {scores[i]} tentative(s)")