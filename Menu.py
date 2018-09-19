import os

os.system('cls')


def display(msg, directory = "null"):
    if (msg == "Welcome"):
        print("""   -----Teretulemast-----""")

    elif (msg == "dir" and directory != "null"):
        print("""     Id  | Name""")
        
        for dir in directory:

            print("""     {}   | {}""".format(directory.index(dir) ,dir))

        print("""   ----------------------
        
        """)

    elif (msg == "List"):
        print("""   -------Project--------""")

    return

def getInput(directory, path):
    selection = input("Vali teema: ")

    if(selection == "help" or selection == "?"):
        print("""   Help:
        Käsklus        | Kirjeldus
        <id ||  nimi>  | Sellega saab minna kausta/ Aktiveerida python faili selle kaustas
        help/?         | Saad informatsiooni erinevate käskluste kohtaä
        quit/q         | Sellega paneb applicatsioon ennast kinni
        """)
        
        getInput(directory, path)
    elif(selection == "quit" or selection == "q"):
        print("""       Goodbye""")
        return
    else:
        try:

            selection = int(selection)

            if (len(directory) > selection):
                try:
                    exec(open(path.replace("\\", "//") + "//" + directory[int(selection)]).read())

                    os.system('cls')
                    display("Welcome")
                    newFiles()

                except FileNotFoundError:
                    newFiles(path + "\\" + directory[int(selection)])
                except PermissionError:
                    newFiles(path + "\\" + directory[int(selection)])

            else:
                print ("Unknown command")
                getInput(directory, path)

        except ValueError:            

            print(directory.index[selection])

            if(directory.index[selection] != -1):
                try:
                    exec(open(path.replace("\\", "//") + "//" + selection).read())

                    os.system('cls')
                    display("Welcome")
                    newFiles()
        
                except FileNotFoundError:
                    newFiles(path + "\\" + directory[int(selection)])
                except PermissionError:
                    newFiles(path + "\\" + directory[int(selection)])

            else:
                print ("Unknown command")
                getInput(directory, path)



def getFiles(inDirectory = os.getcwd()):

    directory = os.listdir(inDirectory)

    if (inDirectory == os.getcwd()):
        directory.remove(".git")
        directory.remove("launcher.bat")
        directory.remove("Menu.py")
        directory.remove(".vs")

    return directory

def newFiles(GoToDir = "null"):

    directory = "null"

    if (GoToDir != "null"):
        os.system('cls')
        directory = getFiles(GoToDir)

        display("dir", directory)

        getInput(directory, GoToDir)

    else:
        directory = getFiles()

        display("dir", directory)

        getInput(directory, os.getcwd())

display("Welcome")
newFiles()








    
