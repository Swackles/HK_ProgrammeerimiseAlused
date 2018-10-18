message = input("Give me messages to eat: ")

newMessage = ""

for char in message:
    newChar = chr(ord(char) + 5)

    if (64 < ord(char) < 91 and not 64 < ord(newChar) < 91 ):
        if (64 > ord(newChar)):
            newChar = chr(90 - ord(newChar) % 64)
        elif (ord(newChar) > 91):
            newChar = chr(65 + (ord(newChar) % 91))
    elif (96 < ord(char) < 123 and not 96 < ord(newChar) < 123 ):
        if (96 > ord(newChar)):
            newChar = chr(122 - ord(newChar) % 96)
        elif (ord(newChar) > 123):
            newChar = chr(97 + (ord(newChar) % 123))

    newMessage = newMessage + newChar

print(newMessage)