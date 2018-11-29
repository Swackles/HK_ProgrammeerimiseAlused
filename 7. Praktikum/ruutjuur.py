import math
import os
import sys

os.system('cls')

# Funktsioon: arvutab ruutjuure
# Sisend: value - arv millest tahad ruutjuurt saada
# Väljund: vastus on *value* ruutjuur
# Eeltingimused: oleks hea kui sisend number
# Järeltingimused: ta annab ruutjuure
def sqrt(value):
    approx = 0.5 * value
    for i in range(int(1E9)):
        try:
            loadingProg([0, 0], [int(i), int(1e9)], False)
        except:
            print("")
        approx = 0.5 * (approx + value/approx)
    return approx


def loadingProg(total, part, totalChange):
    if totalChange:

        print("loading...")
        progressBar = ""
        #total amount to do
        for i in range(total[0]):
            progressBar += "+"
        for i in range(total[1] - total[0]):
            progressBar += "-"
        print(progressBar)

    #1 part of total

    part = [part[0] * 200 / part[1] , 200]

    progressBar = ""
    for i in range(int(part[0])):
        progressBar += "+"
    for i in range(part[1] - int(part[0])):
        progressBar += "-"
    print(progressBar)


sqrtMath = []
sqrtMy = []
original = []

for i in range(19):
    loadingProg([i, 19], [0, 1e9], True)
    sqrtMy.append(sqrt(i + 1))
    sqrtMath.append(math.sqrt(i + 1))
    original.append(i + 1)


row_format ="{:>22}" * 3
print(row_format.format(*["originaal |", "minu |", "math"]))
for original, team, row in zip(original, sqrtMath, sqrtMy):
    print(row_format.format(str(original) + " |", str(team) + " |", row))