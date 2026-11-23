notes = [1000, 500, 100, 50, 20, 10, 5, 2]
amount = int(input("Enter amount : "))

for note in notes:
    if(amount >= note):
        print(f"{amount // note} notes of {note}")
        amount %= note