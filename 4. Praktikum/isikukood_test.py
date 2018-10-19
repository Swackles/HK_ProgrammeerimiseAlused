import isikukood;

DataList = [39105174211, 39401225223, 60002010241, 50002242212, 40803230240, 39506063722, 49210030250, 60004250270, 39410130010, 39506102720, 38705290260, 49601300260]

for item in DataList:

    human = isikukood.Human()

    human.id = str(item)

    human.getDataFromId()

    assert human.check, "Isikukood: " + str(item) + ", andis vea"
    
print("Test oli edukas")