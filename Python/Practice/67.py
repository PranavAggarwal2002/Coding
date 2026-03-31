# m, n = map(int, input().split())

# for i in range(m):
#     arr = list(map(int, input().split()))
#     if i % 2==1:
#         arr.reverse()
#     print(*arr, end=" ")

m, n = map(int, input().split())

result = []

for i in range(m):
    arr = list(map(int, input().split()))
    
    if i % 2 == 1:
        arr.reverse()
    
    result.extend(arr)   # store values

print(*result)