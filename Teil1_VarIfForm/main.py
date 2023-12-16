maxBewertung = 50
maxTische = 10
floatBeispiel = 1.2
stringBeispiel = "Hallo Welt!"

print("Hallo! Willkommen bei Luigis! Wie heißen Sie?")

# Erstellung der Variablen Name und abfragen einer Eingabe des Users über das Terminal!
'''
    Hier steht ein Text!
    Noch eine Zeile!
'''

name = input("Name: ") 

print(f'Hallo {name}!')
print("---------------------------")

print(f"{name}, was möchten Sie tun?")
print("1 - Essensbestellung")
print("2 - Tisch reservieren")
print("3 - Bewertung abgeben")
print("")
wahl = input("Bitte 1, 2 oder 3 eingeben: ")

if(wahl == "1"):
    print("Essensbestellung!")
elif(wahl == "2"):
    print("Tisch reservieren!")
    tisch = input("Bitte Tischnummer eingeben (1-10): ")
    tischInt = int(tisch)
    if(tischInt > 0 and tischInt <= 10):
        print("Tisch reserviert!")
    else:
        print("Falsche Tischzahl!")
elif(wahl == "3"):
    print("Bewertung abgeben!")
    bewertung = input("Bitte deinen Text eingeben: ")
    if(len(bewertung) <= maxBewertung):
        # \n bedeutet Zeilenumbruch im Terminal!
        print("Dein Text: \n" + bewertung)
        bewertungOk = input("Möchtest du diese Bewertung abgeben? 1 - Ja, 2 - Nein ")
        if(bewertungOk == "1"):
            print("Danke für deine Bewertung!")
        else:
            print("Bewertung gelöscht!")
    else:
        print("Deine Bewertung ist zu lang!")
else:
    print("Falsche Eingabe!")

