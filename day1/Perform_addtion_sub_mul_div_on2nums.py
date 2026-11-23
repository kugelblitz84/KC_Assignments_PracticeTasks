firstNum = int(input("Enter first number: "))
secondNum = int(input("enter second num: "))

print(f"Addition of {firstNum} and {secondNum} is: " + str(firstNum + secondNum) + f"\nSubtracting the smaller number from the larger number we get: " + str(max(firstNum, secondNum) - min(firstNum, secondNum)) + f"\nMultiplication of {firstNum} and {secondNum} is: " + str(firstNum * secondNum) + f"\nDivision of {firstNum} and {secondNum} is: " + str(firstNum / secondNum))