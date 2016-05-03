def calcBMI(weight, height):
    BMI = weight / (height * height)
    return BMI

weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in m: "))

BMI = calcBMI(weight, height)

print("Therefore, your BMI value is: {:.2f}".format(BMI))
print("Thank You!")