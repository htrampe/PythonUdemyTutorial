from fragen import *


punkte = 0
maxPunkte = 0

print("Willkommen zum Quiz!")
print("")

for frage in fragen:
    maxPunkte += frage[6]
    print(frage[0])

    # Gibt die Elemente einer Frage von 1 bis 4 untereinander aus!
    for i in range(1,5):
        print(f"{i}. {frage[i]}")

    print("")
    antwort = input("Deine Antwort: ")
    if(antwort == frage[5]):
        print("Richtig!")
        punkte += frage[6]
    else:
        print("Falsch!")

print("")
print(f"Deine Punktzahl ist {punkte} von maximal {maxPunkte}!")