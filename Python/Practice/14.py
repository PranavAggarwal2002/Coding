def pnz(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

nums = list(map(float, input("Enter numbers: ").split()))

for i in nums:
    print(i, "->", pnz(i))