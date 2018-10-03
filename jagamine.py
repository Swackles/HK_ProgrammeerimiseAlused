import os;

os.system("cls");

def getInput(question):
    try:
        number = int(input(question))
    
    except ValueError:
        print("Paluks numbreid")
        
        number  = GetInfo(question)

def main():

    FirstNumber = getInput("Sisesta jagatav: ");
    SecondNumber = getInput("Sisesta jagaja: ");

    if (SecondNumber == 0):
        print("Njah nulliga ei saa eriti midagi teha");
    else:
        Print("Tulemus"+ (FirstNumber / SecondNumber));

if __name__ == '__main__':
    main()