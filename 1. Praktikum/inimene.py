import math
import os

os.system('cls')

class Human():
    age = 0
    height = 0
    weight = 0 
    resultMale = 0
    resultFemale = 0

    def __init__(self, age, height, weight, male = 0, female = 0):
        self.age = age
        self.height = height
        self.weight = weight

        if (male != 0 and female != 0):
            self.resultMale = Result(male[0], male[1], male[2], male[3], male[4])
            self.resultFemale = Result(female[0], female[1], female[2], female[3], female[4])

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__


    def CreateResult(self):

        IdealWeight = [(3 * self.height - 450 + self.age) * 0.25 + 45, (3 * self.height - 450 + self.age) * 0.225 + 40.5]   

        Fat = [(self.weight - IdealWeight[0]) / self.weight * 100 + 15, (self.weight - IdealWeight[1]) / self.weight * 100 + 22]

        Density = [8.9 * Fat[0] + 11 * (100 - Fat[0]), 8.9 * Fat[1] + 11 * (100 - Fat[1])]

        Volume = [self.weight / Density[0], self.weight / Density[1]]

        Area = (1000 * self.weight)**((35.75 - math.log10(self.weight)) / 53.2) * ((self.height**0.3) / 3118.2)

        self.resultMale = Result(round(IdealWeight[0], 2), round(Fat[0], 2), round(Density[0], 2), round(Volume[0], 3), round(Area, 3))
        self.resultFemale = Result(round(IdealWeight[1], 2), round(Fat[1], 2), round(Density[1], 2), round(Volume[1], 3), round(Area, 3))

class Result():
    idealWeight = 0
    fat = 0
    density = 0
    volume = 0
    area = 0

    def __init__(self, idealWeight, fat, density, volume, area):
        self.idealWeight = idealWeight
        self.fat = fat
        self.density = density
        self.volume = volume
        self.area = area

def newHuman():

    def GetInfo(point):

        question = ["Sisesta oma vanus: ", "Sisesta oma pikkus(cm): ", "Sisesta oma kaal (kg): "]
        error = ["Vanus peab olema number", "Pikkus peab olema number", "kaal peab olema number"]

        try:
            info = int(input(question[point]))
    
        except ValueError:
            print(error[point])
        
            info = GetInfo(point)

        return info

    return Human(GetInfo(0), GetInfo(1), GetInfo(2))

def main():

    person = newHuman()
    person.CreateResult()
    PersonData = [person.age, person.height, person.weight]
    Male = [person.resultMale.idealWeight, person.resultMale.fat, person.resultMale.density, person.resultMale.volume, person.resultMale.area]
    Female = [person.resultFemale.idealWeight, person.resultFemale.fat, person.resultFemale.density, person.resultFemale.volume, person.resultFemale.area]

    os.system('cls')

    print("""
    -----Sinu Informatsioon-----
    """)

    row_format ="{:>10}" * (len(["Info"]) + 1)
    print(row_format.format("", *["Info"]))
    for header, info in zip(["Vanus", "Pikkus", "Kaal"], PersonData):
        print (row_format.format(header, info))

    print("""

    ------Arvutuse Tulemus------
    """)

    row_format ="{:>15}" * (len(["Mees", "Naine"]) + 1)
    print(row_format.format("", *["Mees", "Naine"]))
    for Header, Male, Female in zip(["ideaalkaal", "rasvasuse %", "tihedus", "ruumala", "pindala"], Male, Female):
        print (row_format.format(Header, Male, Female))
        
    print("");
    #I have a headache
    if (person.age < 10 or person.age > 85):
        print("Pole ilus internetis valetada");
    elif (person.age >= 10 and person.age <= 16):
        if (person.resultMale.fat < 10):
            print("Mees: Sa peaksid rohkem sööma");
        elif (person.resultMale.fat >= 10 and person.resultMale.fat <= 18):
            print("Mees: Sa sööd täpselt nii palju kui vaja");
        elif (person.resultMale.fat >= 19 and person.resultMale.fat <= 23):
            print("Mees: Rahune maha söögiga");
        elif (person.resultMale.fat > 23):
            print("Mees: Söö vähem ja tee trenni")

        if (person.resultFemale.fat < 18):
            print("Naine: Sa peaksid rohkem sööma");
        elif (person.resultFemale.fat >= 18 and person.resultFemale.fat <= 28):
            print("Naine: Sa sööd täpselt nii palju kui vaja");
        elif (person.resultFemale.fat >= 29 and person.resultFemale.fat <= 35):
            print("Naine: Rahune maha söögiga");
        elif (person.resultFemale.fat > 35):
            print("Naine: Söö vähem ja tee trenni")
    
    elif (person.age >= 17 and person.age <= 39):        
        if (person.resultMale.fat < 12):
            print("Mees: Sa peaksid rohkem sööma");
        elif (person.resultMale.fat >= 12 and person.resultMale.fat <= 20):
            print("Mees: Sa sööd täpselt nii palju kui vaja");
        elif (person.resultMale.fat >= 21 and person.resultMale.fat <= 25):
            print("Mees: Rahune maha söögiga");
        elif (person.resultMale.fat > 25):
            print("Mees: Söö vähem ja tee trenni")

        if (person.resultFemale.fat < 20):
            print("Naine: Sa peaksid rohkem sööma");
        elif (person.resultFemale.fat >= 20 and person.resultFemale.fat <= 32):
            print("Naine: Sa sööd täpselt nii palju kui vaja");
        elif (person.resultFemale.fat >= 33 and person.resultFemale.fat <= 38):
            print("Naine: Rahune maha söögiga");
        elif (person.resultFemale.fat > 38):
            print("Naine: Söö vähem ja tee trenni")

    elif (person.age >= 40 and person.age <= 55):
        if (person.resultMale.fat < 13):
            print("Mees: Sa peaksid rohkem sööma");
        elif (person.resultMale.fat >= 13 and person.resultMale.fat <= 21):
            print("Mees: Sa sööd täpselt nii palju kui vaja");
        elif (person.resultMale.fat >= 22 and person.resultMale.fat <= 26):
            print("Mees: Rahune maha söögiga");
        elif (person.resultMale.fat > 26):
            print("Mees: Söö vähem ja tee trenni")

        if (person.resultFemale.fat < 23):
            print("Naine: Sa peaksid rohkem sööma");
        elif (person.resultFemale.fat >= 23 and person.resultFemale.fat <= 35):
            print("Naine: Sa sööd täpselt nii palju kui vaja");
        elif (person.resultFemale.fat >= 36 and person.resultFemale.fat <= 41):
            print("Naine: Rahune maha söögiga");
        elif (person.resultFemale.fat > 41):
            print("Naine: Söö vähem ja tee trenni")

    elif (person.age >= 56 and person.age <= 85):
        if (person.resultMale.fat < 14):
            print("Mees: Sa peaksid rohkem sööma");
        elif (person.resultMale.fat >= 14 and person.resultMale.fat <= 22):
            print("Mees: Sa sööd täpselt nii palju kui vaja");
        elif (person.resultMale.fat >= 23 and person.resultMale.fat <= 27):
            print("Mees: Rahune maha söögiga");
        elif (person.resultMale.fat > 27):
            print("Mees: Söö vähem ja tee trenni")

        if (person.resultFemale.fat < 24):
            print("Naine: Sa peaksid rohkem sööma");
        elif (person.resultFemale.fat >= 24 and person.resultFemale.fat <= 36):
            print("Naine: Sa sööd täpselt nii palju kui vaja");
        elif (person.resultFemale.fat >= 37 and person.resultFemale.fat <= 42):
            print("Naine: Rahune maha söögiga");
        elif (person.resultFemale.fat > 42):
            print("Naine: Söö vähem ja tee trenni")


if __name__ == '__main__':
    main()