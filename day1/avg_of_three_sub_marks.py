nums = list(map(int, input("Enter three numbers separated by space: ").split()))

avg = sum(nums) / len(nums)
print(f"Average of {nums} is {avg}")