unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temperature = float(input("Enter the temperature: "))

if unit.lower() == "c":
    fahrenheit = (temperature * 9/5) + 32
    print("The temperature in Fahrenheit is", fahrenheit)
elif unit.lower() == "f":
    celsius = (temperature - 32) * 5/9
    print("The temperature in Celsius is", celsius)
else:
    print("Wrong input")