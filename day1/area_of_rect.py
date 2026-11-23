try:
    a, b = map(int, input("Enter length and breadth of rectangle separated by space: ").split())
    print(f"Area of rectangle with length {a} and breadth {b} is {a * b}")
except ValueError as err:
    print("Invalid input. Please enter two integers separated by space.", err)