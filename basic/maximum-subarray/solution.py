class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        import sys
        max_sum = - sys.maxint
        min_sum = 0
        sum = 0
        for num in nums:
            sum+=num
            max_sum = max(max_sum, sum-min_sum)
            min_sum = min(min_sum, sum)

        return max_sum
