# Temperature conversion

unit = input("Is This temperature in celsius or Fehrenheit (C/F): ")
temp = float(input("Enter The Temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°")
else:
    print(f"{unit} is an invalid unit of measurement")


