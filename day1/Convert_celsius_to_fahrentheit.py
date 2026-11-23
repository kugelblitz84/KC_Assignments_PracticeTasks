import sys
import os
def convert_celsius_to_fahrenheit():
    inpt = float(input("Enter temperature in Celsius: "))
    print(f"Converting {inpt}°C to Fahrenheit...")
    fahrenheit = (inpt * 9/5) + 32
    print(f"{inpt}°C is equal to {fahrenheit}°F")
    print("Convert again? (y/n)")
    again = input()
    if(again.lower() == 'y'):
        os.system('cls' if os.name == 'nt' else 'clear')
        convert_celsius_to_fahrenheit()
        
def convert_fahrenheit_to_celsius():
    inpt = float(input("Enter temperature in Fahrenheit: "))
    print(f"Converting {inpt}°F to Celsius...")
    celsius = (inpt - 32) * 5/9
    print(f"{inpt}°F is equal to {celsius}°C")
    print("Convert again? (y/n)")
    again = input()
    if(again.lower() == 'y'):
        os.system('cls' if os.name == 'nt' else 'clear')
        convert_fahrenheit_to_celsius()
        


while 1:
    print("1. Convert Celsius to Fahrenheit\n2. Convert Fahrenheit to Celsius\n3. Exit")
    choice = int(input("Enter your choice: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    match choice:
        case 1: 
            convert_celsius_to_fahrenheit()
        case 2:
            convert_fahrenheit_to_celsius()
        case 3:
            sys.exit(1)
        case _:
            print("Invalid choice. Please try again. or to terminate the program input 3\n")

