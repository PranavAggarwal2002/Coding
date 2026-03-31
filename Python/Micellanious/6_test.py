from collections import defaultdict

def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    
    # Hash map to store frequency of prefix sums
    prefix_map = defaultdict(int)
    prefix_map[0] = 1  # Important for subarrays starting at index 0
    
    for num in nums:
        prefix_sum += num
        
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]
        
        prefix_map[prefix_sum] += 1
    
    return count

