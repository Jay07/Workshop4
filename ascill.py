def getNumber(lower, upper):
    ValidNumber = False
    while not ValidNumber:
        Number = input("Enter a number ({}­{}): ".format(str(lower), str(upper)))
        Number = Number.strip()
        if not Number.isdigit():
            print("Please enter a valid number!")
        elif int(Number) not in range(int(lower), int(upper)):
            print("Please enter a number in range!")
        else:
            ValidNumber = True
    return Number


lower = 50
upper = 120
LowNumber = getNumber(lower, upper)
HighNumber = getNumber(lower, upper)

for i in range(int(LowNumber), int(HighNumber) + 1):
    print("{} {}".format(i, chr(i)))
