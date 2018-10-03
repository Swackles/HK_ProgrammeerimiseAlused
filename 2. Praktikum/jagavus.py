import os;

os.system("cls");

def getInput(question):
    try:
        number = int(input(question))
    
    except ValueError:
        print("Paluks numbreid")
        
        number  = GetInfo(question)

def main():

    FirstNumber = getInput("Sisesta esimene arv: ");
    SecondNumber = getInput("Sisesta teine arv: ");

    if (FirstNumber == 0 or SecondNumber == 0):
        print("Null ei ole sobiv arv");
    elif (FirstNumber >= SecondNumber):
        if ("." in str(FirstNumber / SecondNumber)):
            print("See number ei jagu");
        else:
            print("Tulemus: "+(FirstNumber / SecondNumber));
    elif (SecondNumber <= FirstNumber):
        if ("." in str(SecondNumber / FirstNumber)):
            print("See number ei jagu");
        else:
            print("Tulemus: "+(SecondNumber / FirstNumber));        

if __name__ == '__main__':
    main()