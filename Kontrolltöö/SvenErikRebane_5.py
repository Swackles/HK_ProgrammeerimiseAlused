import os 
file = open(os.path.dirname(os.path.realpath(__file__)) + "\\kt_2.txt", "r")

temperatures = {}

for row in file:
    row = row.replace("\n", "").split(" ")
    if row[1] in temperatures:
        temperatures[row[1]].append(row[0])
    else:
        temperatures[row[1]] = [row[0]]

HighestBelowZero = "null"

for value in temperatures:
    value = int(value)
    if value < 0 and HighestBelowZero == "null":
        HighestBelowZero = value
    elif value < 0 and value > HighestBelowZero:
        HighestBelowZero = value

if HighestBelowZero == "null":
    print("Päevi kus temperatuur oleks langenud alla nulli puududs")
else:
    dates = ""

    for i in range(len(temperatures[str(HighestBelowZero)])):
        value = temperatures[str(HighestBelowZero)][i]
        if i == 0:
            dates = value + "."
        elif i == len(temperatures[str(HighestBelowZero)]) - 1:
            dates += " ja " + value + "."
        else:
            dates += ", " + value + "."

    print("Antud päevade hulgast kõige kõrgem temperatuur, mis on alla 0 kraadi oli " + str(HighestBelowZero) + " kraadi ja see oli: "+dates)

    

    


