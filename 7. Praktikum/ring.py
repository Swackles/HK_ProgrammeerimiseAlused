import math
import ruutjuur

def circleArea(radius):
    return math.pi * (radius**2)

def distanceBetweenPoint(pointX, pointY):
    print(ruutjuur.sqrt(pointX**2 + pointY**2))
    return ruutjuur.sqrt(pointX**2 + pointY**2)

def getuserInput():
    pointA = input("Sisesta keskpunkti kordinaat(xx:yy): ").split(":")
    pointB = input("Sisesta punkti kordinaat teljel(xx:yy): ").split(":")

    return [int(pointA[0]) - int(pointB[0]), int(pointA[1]) - int(pointB[1])]

points = getuserInput()

print(circleArea(distanceBetweenPoint(points[0], points[1])))