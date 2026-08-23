import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"an exception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accgenerator(cls):
        alpha = random.choices(string.ascii_letters,k= 3)
        num = random.choices(string.digits,k=5)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return"".join(id)


    def Createaccount(self):
        info = {
            "name":input("Naam likh: "),
            "age":int(input("Umar likh: ")),
            "email":input("Email likh: "),
            "pin":int(input("Pin likh 4 anko ka: ")),
            "accountNom.":Bank.__accgenerator(),
            "Balance":0
        }

        if info['age']<18 or len(str(info['pin'])) != 4:
            print("Dhatt")
        else:
            print("Account Bani Gayo")
            for i in info:
                print(f"{i}:{info[i]}")
            
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("Account number: ")
        pin = int(input("Enter your 4 digit pin: "))

        userdata = [i for i in Bank.data if i['accountNom.']== accnumber and i['pin']==pin]

        if userdata == False:
            print("Wrong Details")
        else:
            amount = int(input("Enter Amount : "))
            if amount > 10000 or amount < 0:
                print("Errorrrrrrrrrrrrrrrrrrr")
            else:
                userdata[0]['Balance'] += amount
                Bank.__update()
                print("Amount Added Successfully")

    def withdrawmoney(self):
        accnumber = input("Account number: ")
        pin = int(input("Enter your 4 digit pin: "))

        userdata = [i for i in Bank.data if i['accountNom.'] == accnumber and i['pin']== pin]

        if userdata == False:
            print("Errorrrrr")
        else:
            amount = int(input('Enter the Amount: '))
            if userdata[0]['Balance'] < amount:
                print("Enter Valid Amount")
            else:
                userdata[0]['Balance'] -= amount
                Bank.__update()
                print("Amount withdrawn successfully")

    def showdetails(self):
        accnumber = input("Account number: ")
        pin = int(input("Enter your 4 digit pin: "))

        userdata = [i for i in Bank.data if i['accountNom.'] == accnumber and i["pin"]==pin]

        if userdata == False:
            print("errorrrrr")
        else:
            print("Your Information : ")
            for i in userdata[0]:
                print(f"{i}:{userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("Account number: ")
        pin = int(input("Enter your 4 digit pin: "))

        userdata = [i for i in Bank.data if i['accountNom.'] == accnumber and i["pin"]==pin]

        if userdata == False:
            print("errorrr")
        else:
            newdata = {
                "name":input("Enter new name: "),
                "email":input("Enter new email: "),
                "pin":input("Enter new pin: ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]
            
            newdata["age"] = userdata[0]["age"]
            newdata["accountNom."] = userdata[0]["accountNom."]
            newdata["Balance"] = userdata[0]["Balance"]

            if type(newdata["pin"])== str:
                newdata["pin"] = int(newdata["pin"])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            

            Bank.__update()
            print("Details Update Successfully")
    
    def deletedetails(self):
        accnumber = input("Account number: ")
        pin = int(input("Enter your 4 digit pin: "))

        userdata = [i for i in Bank.data if i['accountNom.'] == accnumber and i["pin"]==pin]

        if userdata == False:
            print("errorrr")
        else:
            check = input("Pess Y/N : ")
            if check == 'n' or check == 'N':
                print("Skip")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted Successfully")
                Bank.__update()



user = Bank()  #Object which can access the data of class Bank


print("press 1 for Creating an account")
print("press 2 for Depositing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("Tell your response :- "))

if check == 1:
    user.Createaccount()
if check == 2:
    user.depositmoney()
if check == 3:
    user.withdrawmoney()
if check == 4:
    user.showdetails()
if check == 5:
    user.updatedetails()
if check == 6:
    user.deletedetails()