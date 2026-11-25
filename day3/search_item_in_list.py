lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
item = int(input("Enter the item to search for: "))
for i in range(len(lst)):
    if lst[i] == item:
        print(f"Item found at index: {i}")
        