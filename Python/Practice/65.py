m, n = map(int, input().split())

if m <= 0 or n <= 0:
    print("invalid input")
else:
    minimum = float('inf')   # very large number

    for i in range(m):
        row = list(map(int, input().split()))
        
        for num in row:
            if num < minimum:
                minimum = num

    print(minimum)