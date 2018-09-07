import os

os.system('cls')

def GetWidth():
    try:
        widht = float(input("Sisesta põranda laius (m): "))
    except ValueError:
        print("Põranda laius peab olema number")

        widht = GetWidth()
    return widht

def Getlenght():
    try:
        lenght = float(input("Sisesta põranda pikkus (m): "))
    except ValueError:
        print("Põranda pikkus peab olema number")

        lenght = Getlenght()

    return lenght

def GetPaint():
    try:
        paint = float(input("Sisesta värvikulu kohta (m^2): "))
    except ValueError:
        print("Värvikulu peab olema number")

        paint = GetPaint()
    
    return paint

widht = GetWidth()
lenght = Getlenght()
paint = GetPaint()

os.system('cls')

print("""                      {}m
    +---------------------------------------+
    |                                       |
    |                                       |
    |                                       |
    |                                       | {}m
    |                                       |
    |                                       |
    |                                       |
    +---------------------------------------+

    Ruumala: {}m^2
    Värvi kulub: {}l
""".format(widht, lenght, widht * lenght , (widht * lenght) / paint))

