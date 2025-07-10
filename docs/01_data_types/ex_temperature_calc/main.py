# Temperature conversion


unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input ("Enter the temperature: "))

if unit == "C" or unit =="c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is {temp}F")
elif unit == "F" or unit =="f":
    temp = round((5 * temp) / 9 - 32, 1)
    print(f"The temperature in Fahrenheit is {temp}C")
else:
    print(f"{unit} was not valid")