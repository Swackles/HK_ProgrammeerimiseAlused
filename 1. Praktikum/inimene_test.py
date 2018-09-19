import inimene;

DataList = [
    [22, 178, 75, [71.50, 19.67, 1058.70, 0.071, 1.929], [64.35, 36.20, 1023.98, 0.073, 1.929]]
    ]

for item in DataList:

    result = inimene.Human(item[0], item[1], item[2])

    result.CreateResult()

    correct = inimene.Human(item[0], item[1], item[2], item[3], item[4])

    print("Result  : { 'Age': {"+str(result.age)+"}, 'Height': {"+str(result.height)+"}, 'Weight': {"+str(result.weight)+"}, 'Male': { "+str(vars(result.resultMale))+" }, 'Female': { "+str(vars(result.resultFemale))+" } }")
    print("Correct : { 'Age': {"+str(correct.age)+"}, 'Height': {"+str(correct.height)+"}, 'Weight': {"+str(correct.weight)+"}, 'Male': { "+str(vars(correct.resultMale))+" }, 'Female': { "+str(vars(correct.resultFemale))+" } }")

    print(result == correct)

    assert result == correct, "Damn, mu andmed on valed"