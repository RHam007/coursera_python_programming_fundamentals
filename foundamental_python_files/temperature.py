celsius_temperatures = []
fahrenheit_temperatures = []

celsius_temperatures.extend([0,10,25,32,100])

for celsius in celsius_temperatures:
    fahrenheit = celsius * 1.8 + 32
    fahrenheit_temperatures.append(fahrenheit)
print(fahrenheit_temperatures)
