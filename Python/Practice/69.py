n = int(input())
arr = list(map(int, input().split()))

# Check negative heights
for x in arr:
    if x < 0:
        print("invalid")
        exit()

freq = {}

# Directly compute and count
for i in range(n - 1):
    d = abs(arr[i+1] - arr[i])
    
    if d in freq:
        freq[d] += 1
    else:
        freq[d] = 1

# Find most frequent
max_freq = 0
answer = None

for key in freq:
    if freq[key] > max_freq:
        max_freq = freq[key]
        answer = key

if max_freq == 1:
    print("non")
else:
    print(answer)