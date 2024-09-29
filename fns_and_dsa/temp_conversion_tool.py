FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    try:
        celsius = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
        return celsius
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    try:
        fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
        return fahrenheit
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Main program for user interaction
def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as ve:
        print(ve)

# Run the main function
if __name__ == "__main__":
    main()
