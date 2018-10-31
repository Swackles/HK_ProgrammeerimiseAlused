import os
import calendar

os.system('cls')

class Goal():
    goal = 0
    timeItTakes = 0
    amountWhenGoal = 0

    def __init__(this):
        this.goal = Goal.getGoal()
        

    def getGoal():
        try:
            goal = float(input("Sisesta summa, mida tahad saavutada: "))
    
        except ValueError:
            print("Sisend peab olema number")
        
            goal = Deposit.getGoal()

        return goal

        

class Deposit():
    original = 0
    addEachMonth = 0
    intress = 0
    goal = 0

    def __init__(this):
        this.original = Deposit.getOriginalDeposit()
        this.addEachMonth = Deposit.getAddEachMonth()
        this.intress = Deposit.getIntress() / 12
        this.goal = Goal()

    def getOriginalDeposit():
        try:
            deposit = float(input("Summa, mida soovid hoiusele kanda: "))
    
        except ValueError:
            print("Sisend peab olema number")
        
            deposit = Deposit.getOriginalDeposit()

        return deposit

    def getAddEachMonth():
        try:
            eachMonth = float(input("Summa, mida soovid hoiusele kanda iga kuu alguses: "))
    
        except ValueError:
            print("Sisend peab olema number")
        
            eachMonth = Deposit.getAddEachMonth()

        return eachMonth

    def getIntress():
        try:
            intress = float(input("Sisesta intressimäär aastas: "))
    
        except ValueError:
            print("Sisend peab olema number")
        
            eachMonth = Deposit.getIntress()

        return intress

    def timeToReachGoal(this):

        while this.goal.amountWhenGoal < this.goal.goal:
            this.goal.timeItTakes =+ 1

            this.goal.amountWhenGoal = this.amountWhenGoal * (this.intress / 100) + this.amountWhenGoal + this.addEachMonth

def main():
    deposit = Deposit()

    os.system('cls')

    print(deposit.original)
    print(deposit.addEachMonth)
    print(deposit.intress)
    print(deposit.goal.goal)
    print(deposit.goal.timeItTakes)
    print(deposit.goal.amountWhenGoal)
    
    

if __name__ == '__main__':
    main()
