# Legacy code - left to show progression from what I started with to where I ended

#temperature_c = 25
#temperature_f = 77

#def celsius_to_fahrenheit(celsius):
#    converted_f = (celsius * 9/5) + 32
#    return converted_f

#def fahrenheit_to_celsius(fahrenheit):
#    converted_c = (fahrenheit - 32) * 5/9
#    return converted_c

#def convert_temperature(temperature, unit): # trying to pass 1 of 2 arguments to function call
    
#    if unit == 'C':
#        converted_c = celsius_to_fahrenheit(temperature_c)
#        print(f"{temperature_c}°C is equal to {converted_f}°F")
    
#    elif unit =='F':
#        converted_f = fahrenheit_to_celsius(temperature_f)
#        print(f"{temperature_f}°F is equal to {converted_c}°C")
#    else:
#        raise ValueError("Invalid unit.  Please use 'C' or 'F'")
    

#converted_f = convert_temperature(temperature_c, 'C')
#converted_c = convert_temperature(temperature_f, 'F')

# Corrected code with docstring and note(s)
# Made temperature and symbol user prompts.

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    converted_f = (celsius * 9/5) + 32
    return converted_f

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    converted_c = (fahrenheit - 32) * 5/9
    return converted_c

def convert_temperature(temperature: float, unit: str) -> float:
    """
    Convert temperature between Celsius and Fahrenheit.

    Parameters:
    temperature (float): The temperature to convert.
    unit (str): The unit of the temperature ('C' for Celsius and 'F' for Fahrenheit).

    Returns:
    float: The converted temperature.
    """
    
    if unit == 'C':
        converted_f = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_f:.2f}°F")
        return converted_f
    
    elif unit == 'F':
        converted_c = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_c:.2f}°C")
        return converted_c
    else:
        raise ValueError("Invalid unit. Please use 'C' or 'F'.")

# User prompts for temperature and scale (C or F)
temperature_input = float(input('Please enter the temperature to convert: '))
scale_input = input("Enter either 'C'elcius or 'F'ahrenheit: ")

try:
    converted_f = convert_temperature(temperature_input, scale_input)
except ValueError as e:
    print(e)