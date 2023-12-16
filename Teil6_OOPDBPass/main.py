from cryptography.fernet import Fernet
import sqlite3

from password import Password

passwords = []
masterkey = b'LiM-Rnhfuoju1lPACO3LqINiTDdnXBkKn0ldBDY-Vlw='

def createConnection():
    return sqlite3.connect("passwords.db")

def createTables():
    con = createConnection()
    cur = con.cursor()
    cur.execute("create table if not exists passwords(service, key, hint)")
    con.close()

def encryptKey(key):
    f = Fernet(masterkey)
    return f.encrypt(key.encode())

def createNewPassword():
    print("Neues Passwort erstellen")
    service = input("Bitte Service eingeben: ")
    key = input("Bitte Key eingeben: ")
    hint = input("Bitte Hinweis eingeben (oder Enter für keinen Hinweis): ")
    con = createConnection()
    cur = con.cursor()
    cur.execute(f"insert into passwords values ('{service}', '{encryptKey(key).decode()}', '{hint}')")
    con.commit()
    con.close()
    mainMenu()

def getAllPasswords():
    global masterkey
    localPasswords = []
    fernet = Fernet(masterkey)
    con = createConnection()
    cur = con.cursor()
    result = cur.execute("select * from passwords")
    for r in result:
        localPasswords.append(Password(service=r[0], key=r[1].encode(), hint=r[2]))
    return localPasswords   

def showAllPasswords():
    global passwords
    passwords = getAllPasswords()
    for password in passwords:
        print(f"Service: {password} und das PW lautet {password.getDecryptKey(masterkey).decode()}")
        print(f"         Hinweis: {password.hint}")

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

#showAllPasswords()
mainMenu()
#createConnection()
#createTables()