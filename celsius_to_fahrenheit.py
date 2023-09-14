def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Ask the user for input
choice = input("Choose conversion type (C to F or F to C): ").strip().upper()

# Perform the conversion based on user's choice
if choice == "C TO F":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
    
elif choice == "F TO C":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")
    
else:
    print("Invalid choice. Please choose 'C to F' or 'F to C'.")
