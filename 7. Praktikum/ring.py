import math
def sqrt(value):
    approx = 0.5 * value
[]    for i in range(int(1e9)):
        approx = 0.5 * (approx + value/approx)
    return approx

def circleArea(radius):
    return math.pi * (radius**2)

def distanceBetweenPoint(pointX, pointY):
    print(sqrt(pointX**2 + pointY**2))
    return sqrt(pointX**2 + pointY**2)

def getuserInput():
    pointA = input("Sisesta keskpunkti kordinaat(xx:yy): ").split(":")
    pointB = input("Sisesta punkti kordinaat teljel(xx:yy): ").split(":")

    return [int(pointA[0]) - int(pointB[0]), int(pointA[1]) - int(pointB[1])]

points = getuserInput()


print(circleArea(distanceBetweenPoint(points[0], points[1])))

array = [[temp, kuu1, kuu2...], [temp, kuu1, kuu2...], [temp, kuu1, kuu2...]]
array = [[temp, [kuu1, kuu2...]], [temp, [kuu1, kuu2...]], [temp, [kuu1, kuu2...]]]
array = {temp = [kuu1, kuu2...], temp = [kuu1, kuu2...]}

array = [temp1, temp2, temp3]
array = [[kuu1, kuu2], [kuu3], [kuu4, kuu5, kuu6]]