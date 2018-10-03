
import os;
import math;

os.system("cls");

def getInput():
    try:
        number = int(input("Sisesta positiivne arv?: "))
        
        if (number <= 0):
            print("Paluks midagi suuremat kui 0");

            number = getInput();
    except ValueError:
        print("Paluks numbreid")
        
        number  = getInput()

    return number;

def main():

    number = getInput();

    if(".0" in str(number / 4) or (".0" in str(number / 100) and not (".0" in str(number / 400)))):
        print("Tegemist on liigaastaga");
    else:
        print("Tegemist on lihtaastaga");

if __name__ == '__main__':
    main()