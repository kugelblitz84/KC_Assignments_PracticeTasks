
try:
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    print(f"The largest number in the list {lst} is: {max(lst)}")
except ValueError as err:
    print("Invalid input. Please enter integers separated by spaces. " + str(err))
