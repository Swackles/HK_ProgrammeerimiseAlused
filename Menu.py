import os

os.system('cls')

print("""   -----Teretulemast-----""")

currentDir = os.getcwd()

directory = os.listdir()

directory.remove(".git")
directory.remove("launcher.bat")
directory.remove("Menu.py")

print("""     Id  | Name""")

for dir in directory:
    print("""     {}   | {}""".format(directory.index(dir) ,dir))

print("""   ----------------------

""")

selection = input("Vali teema: ")
if (directory.index[selection]

if (type[selection] is int:
    try:
        selection = int(selection)
    catch ValueError:
        print("What vodoo is this")

if (type[selection] is str:
    exec(open(currentDir,"//",directory).read())
    
