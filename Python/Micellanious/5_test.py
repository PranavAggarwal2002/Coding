def subarraySum(nums, k):
    count = 0
    n = len(nums)

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == k:
                count += 1

    return count
