class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        import sys
        max_sum = -sys.maxint
        min_sum = 0
        sum = 0
        for num in nums:
            sum+=-num
            max_sum = max(max_sum, sum - min_sum)
            min_sum = min(min_sum, sum)

        return -max_sum
