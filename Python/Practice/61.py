# Q1. The Chrono-Locked Conveyor Belt
#
# In an ancient mechanical city, a circular conveyor belt transports crystalline
# energy cores in a strictly non-decreasing sequence of stability levels.
#
# The belt was originally arranged in sorted (non-decreasing) order to prevent
# resonance collapse. However, during a maintenance cycle, the system restarted
# from an arbitrary position, making the sequence appear rotated.
#
# Your task is to determine whether the current sequence can represent a valid
# rotation of a non-decreasing sorted array.
#
# Conditions:
# • The original array was sorted in non-decreasing order.
# • The array may be rotated any number of times (including zero).
# • Duplicate values are allowed.
# • If the sequence does not follow this property, return False.
#
# Return:
# • True  → if the sequence is a valid rotated sorted array
# • False → otherwise
#
# Example Test Cases:
# Input:  [5,6,7,1,2,3,4]   → Output: True
# Input:  [2,2,2,3,1,2]     → Output: True
# Input:  [1,3,2,4]         → Output: False
# Input:  [10,10,10]        → Output: True
# Input:  [4,5,1,2,6]       → Output: False

def is_rotated_sorted(arr):
    count = 0
    n = len(arr)

    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count += 1
        if count > 1:
            return False

    return True


# Test cases
print(is_rotated_sorted([5,6,7,1,2,3,4]))  # True
print(is_rotated_sorted([2,2,2,3,1,2]))    # True
print(is_rotated_sorted([1,3,2,4]))        # False
print(is_rotated_sorted([10,10,10]))       # True
print(is_rotated_sorted([4,5,1,2,6]))      # False