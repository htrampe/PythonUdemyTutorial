import random

def getRandomResultLoose():
    spruecheVerloren = ["Das war ganz schwach!", "Schade!", "Schon wieder verloren...?"]
    return spruecheVerloren[random.randint(0,len(spruecheVerloren)-1)]

def getRandomResultWin():
    spruecheGewonnen = ["Das war mega!", "Super!", "Ich habe keine Chance"]
    return spruecheGewonnen[random.randint(0,len(spruecheGewonnen)-1)]

def getUserInput():
    try:
        userNummer = int(input("Deine Zahl: "))
        return userNummer
    except:
        print("Falche Nummer!")
        return False

def getPCNumber():
    return random.randint(1,10)

def startLuckyNumbers():
    print("Lucky Numbers!")
    nutzerZahl = getUserInput()
    if(nutzerZahl != False):
        pcNumber = getPCNumber()
        if(pcNumber == nutzerZahl):
            print(f"Deine Zahl war {nutzerZahl}, der PC hatte die {pcNumber}! Du hast gewonnen!", getRandomResultWin())
        else:
            print(f"Deine Zahl war {nutzerZahl}, der PC hatte die {pcNumber}! Du hast leider verloren!", getRandomResultLoose())
        startLuckyNumbers()
    else:
        startLuckyNumbers()

startLuckyNumbers()