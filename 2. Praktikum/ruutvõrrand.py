import os;
import math;

os.system("cls");

class quadratic():
    a = 0;
    b = 0;
    c = 0;
    x1 = 0;
    x2 = 0;
    completed = 0;

    def __init__(self, a, b, c):
        self.a = a;
        self.b = b;
        self.c = c;

    def calculate(self):
        x = self.b ** 2 - 4 * self.a * self.c;

        if (x >= 0):
            x = math.sqrt(x);

            self.x1 = round((-self.b + x) / (2 * self.a), 2);
            self.x2 = round((-self.b - x) / (2 * self.a), 2);

            self.completed = True;
        else:
            self.completed = False;

        return self;

def getInput(question):
    try:
        number = int(input(question))

        if (number <= 0):
            print("Number ei saa olla alla 0");

            number = getInput(question);
    
    except ValueError:
        print("Paluks numbreid")
        
        number  = getInput(question)

    return number;

def main():

    print("Ruutvõrrand: ax^2 + bx + c = 0")

    value = quadratic(getInput("Sisesta a väärtus: "), getInput("Sisesta b väärtus: "), getInput("Sisesta c väärtus: "))

    value = value.calculate();

    os.system('cls');

    print(str(value.a)+"x^2 + "+str(value.b)+"x + "+str(value.c)+" = 0")

    if (value.completed):
        print("x1 = "+str(value.x1));
        print("x2 = "+str(value.x2));
    else:
        print("reaalarvulised lahendid puuduvad");

if __name__ == '__main__':
    main()