import os;

os.system("cls");

def main():

    sticks = [];
    
    while (len(sticks) != 3):
        try:
            number = int(input("Sisesta külje pikkus"))

            sticks.append(number);
    
        except ValueError:

            print("Paluks numbreid")

    hypotenuse = 0;
    sum = 0

    for stick in sticks:
        if (stick > hypotenuse):
            if (sum != 0):
                sum -= stick;
            hypotenuse = sticks;
        else:
            sum += stick;

    sticks.remove(hypotenuse);
    
    if (hypotenuse < sum):
        print("Nende arvudega saab kolmnurga ehitada");
    else:
        print("Nende arvudega ei saa kolmnurga ehitada");

if __name__ == '__main__':
    main()