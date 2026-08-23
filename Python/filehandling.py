from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))

    for i, items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():
    try:
        readfileandfolder();
        name = input("FILE NAME :- ")
        p = Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data = input("ADD TEXT :- ")
                fs.write(data)

            print(F"FILE CREATED SUCCESSFULLY")
        else:
            print("File already exists!!!!!!!!!")

    except Exception as err:
        print(f"An error occured as {err}")

def readFile():
    try:
        readfileandfolder()
        name = input("FILE NAME :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("FILE READED SUCCESSFULLY")
        else:
            print("File does not exists!!!!!!!!!")
    except Exception as err:
        print(f"An error occured as {err}")

def updateFile():
    try:
        readfileandfolder()

        name = input("FILE NAME :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("PRESS 1 FOR FILE NAME CHANGE")
            print("PRESS 2 FOR UPDATING THE DATA OF FILE")
            print("PRESS 3 FOR APPENDING")
            
            res = int(input('CHOOSE A NUMBER :- '))

            if res == 1:
                name2 = input("NEW FILE NAME :- ")
                p2 = Path(name2)
                p.rename(p2)
                print("FILE NAME CHANGED SUCCESSFULLY")
            if res == 2:
                with open(p,'w') as fs:
                    data = input("Start typing :- ")
                    fs.write(data)
                    print("DATA UPDATED SUCCESSFULLY")
            if res == 3:
                with open(p,'a') as fs:
                    data = input("Start typing :- ")
                    fs.write(" " + data)
                    print("DATA ADDED SUCCESSFULLY")
        else:
            print("File does not exists!!!!!!!!!")

    except Exception as err:
        print(f"An error occured as {err}")

def deleteFile():
    try:
        readfileandfolder()
        name = input("FILE NAME :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)

            print("FILE DELTED SUCCESSFULLY")
        else:
            print("File does not exists!!!!!!!!!")
    except Exception as err:
        print(f"An error occured as {err}")


print('PRESS 1 FOR CREATING A FILE')
print('PRESS 2 FOR READING A FILE')
print('PRESS 3 FOR UPDATING A FILE')
print('PRESS 4 FOR DELETING A FILE')

check = int(input('CHOOSE A NUMBER :- '))

if check == 1:
    createfile()
if check == 2:
    readFile()
if check == 3:
    updateFile()
if check == 4:
    deleteFile()