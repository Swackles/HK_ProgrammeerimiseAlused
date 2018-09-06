import math
import os

os.system('cls')
def GetAge():
    try:
        age = int(input("Sisesta oma vanus: "))
    
    except ValueError:
        print("Vanus peab olema number")
        
        age = GetAge()

    return age

def GetHeight():
    try:
        height = int(input("Sisesta oma pikkus(cm)"))
    
    except ValueError:
        print("Pikkus peab olema number")

        height = GetHeight()

    return height

def GetWeight():
    try:
        weight = float(input("Sisesta oma kaal (kg)"))

    except ValueError:
        print("kaal peab olema number")

        weight = GetWeight()
    
    return weight

def GetGender():
    gender = input("Sisesta sugu (m/n)")

    if (gender != "m" and gender != "n"):
        gender = GetGender() 

    return gender

age = GetAge()
height = GetHeight()
gender = GetGender()
weight = GetWeight()

def IdealWeight(age, height, gender):

    if (gender == "m"):
        ideal = (3 * height - 450 + age) * 0.25 + 45

    elif (gender == "n"):
        ideal = (3 * height - 450 + age) * 0.225 + 45
    
    return ideal

def FatPercent(weight, idealWeight, gender):

    if (gender == "m"):
        fatPercent = (weight - idealWeight) / weight * 100 + 15 

    elif (gender == "n"):
        fatPercent = (weight - idealWeight) / weight * 100 + 22

    return fatPercent

def Density(fat):
    density = 8.9 * fat + 11 * (100 - fat)

    return density

def Volume(weight, density):
    volume = weight / density

    return volume

def Area(weight, height):
    area = (1000 * weight)**((35.75 - math.log10(weight)) / 53.2) * ((height**0.3) / 3118.2)

    return area

os.system('cls')

print("""Sinu informatsioon:

    Age - {}
    Height - {}m
    Gender - {}
    Weight - {}kg
""".format(age, height, gender, weight))

idealWeight = IdealWeight(age, height, gender)
fatPercent = FatPercent(weight, idealWeight, gender)
density = Density(fatPercent)
volume = Volume(weight, density)
area = Area(weight, height)

def WeightSit(currentWeight, idealWeight):
    if (currentWeight > idealWeight):
        situation = "Su hetkene kaal on suurem kui ideaal kaal"
    elif (currentWeight < idealWeight):
        situation = "Su hetkene kaal on väiksem kui ideaal kaal"
    else:
        situation = "Su hetkene kaal ja ideaal kaal on sama"

    return situation

weightSit = WeightSit(weight, idealWeight)

print("""    ------------------------------------------

    Ideaal kaal - {}kg
        {}
    Rasva Protsent - {}%
    Rasva Tihedus - {}kg/m^3
    Ruumala - {}m^3
    Pindala - {}m^2
""".format(idealWeight, weightSit, fatPercent, density, volume, area))