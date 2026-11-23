try :
    num = int(input("Enter a number: "))
    print("The number is positive" if num > 0 else "the number is negative" if num < 0 else "the number is zero")
except ValueError as err:
    print("Invalid input. Please enter a valid integer." + str(err))