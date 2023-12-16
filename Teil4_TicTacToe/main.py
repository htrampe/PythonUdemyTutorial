# Erstellt eine Liste mit 9 " " Elementen
field = [" " for i in range(9)]
player = 1

# Prüft, ob übergebene Feldnummer leer ist
def isFieldEmpty(fieldToCheck):
    return field[fieldToCheck] == " "
    '''
    # Lange Methode
    if(field[fieldToCheck] == " "):
        return True
    else:
        return False
    '''

# Prüft auf gültigem UserInput 1 bis 9, gibt die Zahl zurück oder False bei ungültiger Prüfung!
def getUserInput():
    try:
        userNummer = int(input("Deine Zahl: "))
        if(userNummer >= 1 and userNummer <= 9):
            return userNummer
        else:
            return False
    except:
        return False

# Gibt True zurück, wenn es noch leere Felder gibt, ansonsten False
def emptyFields():
    emtpy = False
    for f in field:
        if(f == " "):
            emtpy = True
    return emtpy

# Prüft auf einen Gewinner!
def checkWin():
    # Prüfung oberste Reihe
    if((field[0] == "X" and field[1] == "X" and field[2] == "X") or (field[0] == "O" and field[1] == "O" and field[2] == "O")):
        print("Es gibt einen Gewinner!")
    # Prüfung mittlere Reihe
    elif((field[3] == "X" and field[4] == "X" and field[5] == "X") or (field[3] == "O" and field[4] == "O" and field[5] == "O")):
        print("Es gibt einen Gewinner!")
    # Prüfung unterste Reihe
    elif((field[6] == "X" and field[7] == "X" and field[8] == "X") or (field[6] == "O" and field[7] == "O" and field[8] == "O")):
        print("Es gibt einen Gewinner!")
    # Prüfung Spalte Links
    elif((field[0] == "X" and field[3] == "X" and field[6] == "X") or (field[0] == "O" and field[3] == "O" and field[6] == "O")):
        print("Es gibt einen Gewinner!")
    # Prüfung Spalte Mitte
    elif((field[1] == "X" and field[4] == "X" and field[7] == "X") or (field[1] == "O" and field[4] == "O" and field[7] == "O")):
        print("Es gibt einen Gewinner!")
    # Prüfung Spalte Rechts
    elif((field[2] == "X" and field[5] == "X" and field[8] == "X") or (field[2] == "O" and field[5] == "O" and field[8] == "O")):
        print("Es gibt einen Gewinner!")
    # Diagonale Links oben Rechts unten
    elif((field[0] == "X" and field[4] == "X" and field[8] == "X") or (field[0] == "O" and field[4] == "O" and field[8] == "O")):
        print("Es gibt einen Gewinner!")
    # Diagonale Rechts oben Links unten
    elif((field[2] == "X" and field[4] == "X" and field[6] == "X") or (field[2] == "O" and field[4] == "O" and field[6] == "O")):
        print("Es gibt einen Gewinner!")
    else:
        if(emptyFields()):
            choosePlayer()
        else:
            print("Keine freien Felder! Spiel vorbei!")

# Zeichnet das Spielfeld
def drawField():
    print("#############")
    print("#",field[0],"#",field[1],"#",field[2],"#")
    print("#",field[3],"#",field[4],"#",field[5],"#")
    print("#",field[6],"#",field[7],"#",field[8],"#")
    print("#############")
    checkWin()

# Nimmt entsprechenden Spieler dran und ändert das Feld!
def choosePlayer():
    global player
    if(player == 1):
        print("Player 1(X) bitte eine Feldnummer eingeben (1-9): ", end="")
        pfield = getUserInput()
        if(pfield == False):
            print("Falsche Eingabe! Bitte nur 1-9 eingeben!")
            choosePlayer()
        else:
            pfield -= 1
            if(isFieldEmpty(pfield)):
                field[pfield] = "X"
                player = 2
                drawField()
            else:
                print("Feld nicht leer!")
                choosePlayer()
    elif(player == 2):
        print("Player 2(O) bitte eine Feldnummer eingeben (1-9): ", end="")
        pfield = getUserInput()
        if(pfield == False):
            print("Falsche Eingabe! Bitte nur 1-9 eingeben!")
            choosePlayer()
        else:
            pfield -= 1
            if(isFieldEmpty(pfield)):
                field[pfield] = "O"
                player = 1
                drawField()
            else:
                print("Feld nicht leer!")
                choosePlayer()

# Startet das Spiel!
def startTicTacToe():
    print("TicTacToe starten!")
    print("------------------")
    drawField()

startTicTacToe()