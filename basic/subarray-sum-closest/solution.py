class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        n = len(nums)
        prefix_sum = []
        sum = 0
        for index in range(n):
            sum+=nums[index]
            prefix_sum.append((sum, index))

        sorted_prefix_sum = sorted(prefix_sum)
        import sys
        min_sum = -sys.maxint
        closet_index = 0
        for index in range(1,n):
            diff_sum = abs(sorted_prefix_sum[index-1][0] - sorted_prefix_sum[index][0])
            if diff_sum < min_sum:
                min_sum = diff_sum
                closet_index = index-1

        left_index = min(sorted_prefix_sum[closet_index-1][1], sorted_prefix_sum[closet_index][1])

        right_index = max(sorted_prefix_sum[closet_index-1][1], sorted_prefix_sum[closet_index][1])

        return [left_index+1, right_index]
