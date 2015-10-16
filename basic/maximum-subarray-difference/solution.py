class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    def get_max_sum(self, nums, order=0):
        import sys
        n = len(nums)
        sum = 0
        min_sum = 0
        result = [0 for i in range(n)]
        indexs = [i for i in range(n)]
        if order != 0:
            indexs.reverse()

        sum = 0
        min_sum = 0
        max_sum = -sys.maxint
        for index in indexs:
            sum+= nums[index]
            max_sum = max(max_sum, sum - min_sum)
            min_sum = min(min_sum, sum)
            result[index] = max_sum

        return result

    def maxDiffSubArrays(self, nums):
        # write your code here
        import sys
        n = len(nums)
        left_max = self.get_max_sum(nums, 0)
        left_min = self.get_max_sum([-num for num in nums], 0)
        right_max = self.get_max_sum(nums,1)
        right_min = self.get_max_sum([-num for num in nums], 1)

        max_diff = -sys.maxint
        for i in range(n-1):
            max_diff_1 = abs(left_max[i] - right_min[i+1])
            max_diff_2 = abs(left_min[i] - right_max[i+1])
            max_diff = max(max_diff, max_diff_1, max_diff_2)

        return max_diff

