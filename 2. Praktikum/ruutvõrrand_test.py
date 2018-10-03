import ruutvõrrand;
import os;

DataList = [[2, 5, 2, True, -0.5, 2], [3, 2, -1, True, 0.33, -1], [2, 2, 2, False, 0, 0], [2, 4, 2, True, -1, -1]]

for item in DataList:

    result = ruutvõrrand.quadratic(item[0], item[1], item[2])

    correct = result.calculate();

    result.completed = item[3];
    result.x1 = item[4];
    result.x2 = item[5];

    assert result == correct, "Test failed"

    print("Test was successfull");
