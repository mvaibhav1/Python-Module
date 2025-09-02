def temperature_converter(celsius):
    farheniet=(celsius*1.8) +32
    return farheniet

c=float(input("Enter  the temperature in celsius : "))
print(f"The temperature in Farheniet is {temperature_converter(c)}")