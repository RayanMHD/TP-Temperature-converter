F = float(input("Please type in a temperature (F): "))
C = (F - 32) * 5 / 9

print(f"{F} degrees Fahrenheit equals {C} degrees Celsius")

if C < 0:
    print("Brr! It's cold in here!")