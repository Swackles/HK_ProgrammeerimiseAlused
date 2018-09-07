import os

os.system('cls')

print("""   -----Teretulemast-----""")

directory = os.listdir()

directory.remove(".git")
directory.remove("launcher.bat")
directory.remove("Menu.py")

print("""     Id  | Name""")

for dir in directory:
    print("""     {}   | {}""".format(directory.index(dir) ,dir))

print("""   ----------------------

""")

selection = input("Vali teema (kas id või nimi): ")

print(typeof(selection))