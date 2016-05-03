def calcArea(width, height):
    area = width * height
    return area

width = float(input("Enter width: "))
height = float(input("Enter height: "))

area = calcArea(width, height)


print("Area:", int(area))