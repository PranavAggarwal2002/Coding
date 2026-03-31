def is_rotated_sorted(arr):
    count = 0
    n = len(arr)

    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count += 1
        
        if count > 1:
            return False

    return True