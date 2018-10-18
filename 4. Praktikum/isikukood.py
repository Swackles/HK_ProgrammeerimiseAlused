import os
import datetime
import math
from datetime import date

os.system('cls')

class Human():
    id = ""
    birthday = ""
    age = ""
    gender = ""
    check = False

    def getId(self):
        try:
            id = int(input("Sisesta isikukood: "))

        except ValueError:
            print("No number pls")
        
            id = GetInfo()

        self.id = str(id)

    def getDataFromId(self):
        if (int(self.id[:1]) % 2 == 0):
            self.gender = "F"    
        
        else:
            self.gender = "M"

        year = [1800, 1800, 1900, 1900, 2000, 2000]

        self.birthday = str(year[int(self.id[:1])] + int(self.id[1:3])) +"/"+ self.id[3:5] +"/"+ self.id[5:7]

    def getAge(self):
        currentDate = datetime.datetime.today().strftime('%Y-%m-%d').split("-")
        currentDate = date(int(currentDate[0]), int(currentDate[1]), int(currentDate[2]))
        birthday = self.birthday.split("/")
        birthdayDate = date(int(birthday[0]), int(birthday[1]), int(birthday[2]))

        self.age = math.floor((currentDate - birthdayDate).days / 365)

    def test(self):
        testnumber = 0
        i = 1
        for char in self.id:
            if i == 10:
                testnumber = testnumber + (int(char) * 1)
            elif i > 10:
                print(char)
                print(testnumber)
                print(testnumber % 11)
                if testnumber % 11 == int(char):
                    self.check = True
            else:
                testnumber = testnumber + (int(char) * i)

            i = i + 1
        





def main():
    person = Human()
    person.getId()
    person.getDataFromId()
    person.getAge()
    person.test()
    print(person.id)
    print(person.birthday)
    print(person.gender)
    print(person.age)
    print(person.check)


if __name__ == '__main__':
    main()