def convertFahrenheit(tempCelsius):
    tempFahrenheit = (tempCelsius * 1.8) + 32
    return tempFahrenheit

tempCelsius = float(input("Enter temperature in Celsius: "))

tempFahrenheit = convertFahrenheit(tempCelsius)

print("Temperature in Fahrenheit:", tempFahrenheit)