class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        import sys
        n = len(nums)
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]
        max_sum = -sys.maxint
        min_sum = 0
        sum = 0
        for index in range(n):
            sum+= nums[index]
            max_sum = max(max_sum, sum - min_sum)
            min_sum = min(sum, min_sum)
            left[index] = max_sum

        sum = 0
        min_sum = 0
        max_sum = -sys.maxint
        for index in range(n-1, -1, -1):
            sum+= nums[index]
            max_sum = max(max_sum, sum - min_sum)
            min_sum = min(sum, min_sum)
            right[index] = max_sum

        max_sum = -sys.maxint
        for i in range(n-1):
            max_sum = max(left[i] + right[i+1], max_sum)

        return max_sum
