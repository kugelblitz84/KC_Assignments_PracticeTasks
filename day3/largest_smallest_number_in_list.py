lst = list(map(int, input("Enter numbers seprated by space: ").split()))

mn = mx = lst[0]

for i in lst:
    mn = min(mn, i)
    mx = max(mx, i)

print(f"smallest: {mn}, largest: {mx}")