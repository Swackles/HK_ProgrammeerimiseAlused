import os

os.system('cls')

def getMath():

    try:
        math = int(input("Sisesta matemaatika riigieksami tulemus (punktides): "))

    except ValueError:
        print("Nojah, tahaks saada nagu numrit")

        math = getMath()

    return math

def getLang():

    try:
        lang = int(input("Sisesta eesti keele riigieksami tuleus (punktids)"))

    
    except ValueError:
        print("Nojah, tahaks saada nagu numrit")

        lang = getLang()

    return lang

def getRequiredPoint(math, lang):
    
    bigMath = (math * 25) / 100
    bigLang = (lang * 25) / 100

    requiredPoint = (65 - bigMath - bigLang) * 2
    
    return requiredPoint

math = getMath()
lang = getLang()

os.system('cls')

requiredPoint = getRequiredPoint(math, lang)


if requiredPoint > 100:
    print("""   Sinu tulemused:
    
        Matemaatika riigieksam: {} punkti
        Eesti keele riigieksam: {} punkti

        --------------------------

        Sul ei ole lootust et sisse saada
        aga kui tahad teada kui palju oleks vaja on tulemus {}
    """.format(math, lang, requiredPoint))
else:
        print("""   Sinu tulemused:
        Matemaatika riigieksam: {} punkti
        Eesti keele riigieksam: {} punkti

        --------------------------

        Sul on vaja {} punkti vastuvõtu eksamil, et sisse saada
    """.format(math, lang, requiredPoint))