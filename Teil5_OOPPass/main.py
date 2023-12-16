from cryptography.fernet import Fernet

from password import Password

passwords = []
masterkey = b'LiM-Rnhfuoju1lPACO3LqINiTDdnXBkKn0ldBDY-Vlw='

def encryptKey(key):
    f = Fernet(masterkey)
    return f.encrypt(key.encode())

def createDemoData():
    passwords.append(Password(service="Google", key=encryptKey("123")))
    passwords.append(Password(service="Mila", key=encryptKey("123")))
    passwords.append(Password(service="Apple", key=encryptKey("123")))
    passwords.append(Password(service="MeineFirma", key=encryptKey("123"), hint="Das mit A"))
    passwords.append(Password(service="MeineBank", key=encryptKey("123")))

def createNewPassword():
    print("Neues Passwort erstellen")
    print("")
    service = input("Bitte Service eingeben: ")
    key = input("Bitte Key eingeben: ")
    hint = input("Bitte Hinweis eingeben (oder Enter für keinen Hinweis): ")
    passwords.append(Password(service = service, key = encryptKey(key), hint= hint))
    mainMenu()

def showAllPasswords():
    for password in passwords:
        print(password)
        print(password.getDecryptKey(masterkey))
        print(password.key)

    mainMenu()

def mainMenu():
    print("Wähle aus!")
    print("1 - Neues Passwort erstellen")
    print("2 - Alle Passwörter ausgeben")
    choice = input("Deine Auswahl: ")
    if(choice == "1"):
        createNewPassword()
    elif(choice == "2"):
        showAllPasswords()
    else:
        print("Falsche Auswahl!")
        mainMenu()

mainMenu()