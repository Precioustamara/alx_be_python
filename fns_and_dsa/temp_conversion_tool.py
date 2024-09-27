# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using global conversion factor.
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using global conversion factor.
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius + FAHRENHEIT_OFFSET) * CELSIUS_TO_FAHRENHEIT_FACTOR

def main():
    try:
        # Get temperature input from user
        temp = input("Enter the temperature value: ")
        if not temp.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temp = float(temp)

        # Get unit of the temperature
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp: }°F.")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp: }°C.")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
