
import asyncio
from asyncio import sleep
import os

def again():
    print("Do you want to perform another calculation? (y/n)")
    return input().lower() == 'y'

async def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("====Calculator====")
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        try:
            c = int(input("Enter your choice (1/2/3/4/5): "))
            match c:
                case 1:
                    a = int(input("Enter first number: "))
                    b = int(input("Enter second number: "))
                    print(f"Result: {a + b}")
                    if not again():
                        break
                case 2:
                    a = int(input("Enter first number: "))
                    b = int(input("Enter second number: "))
                    print(f"Result: {a - b}")
                    if not again():
                        break
                case 3:
                    a = int(input("Enter first number: "))
                    b = int(input("Enter second number: "))
                    print(f"Result: {a * b}")
                    if not again():
                        break
                case 4:
                    a = int(input("Enter first number: "))
                    b = int(input("Enter second number: "))
                    try:
                        print(f"Result: {a / b}")
                        if not again():
                            break
                    except ZeroDivisionError as err:
                        print(f"Error: {err}", flush = True)
                        await sleep(2)
                case 5:
                    print("Exiting the calculator.")
                    break
                case _:
                    print("Invalid choice. Please try again.")
                    await sleep(2)
        except ValueError:
            print("Invalid input. Please enter a number.")
            await sleep(2)
                    
                    

if __name__ == "__main__":
    # import asyncio
    asyncio.run(main())