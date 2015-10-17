class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        n = len(nums)
        prefix_sum = []
        sum = 0
        for num in nums:
            sum+=num
            prefix_sum.append(sum)

        hash = {0:-1}
        for index in range(n):
            sum = prefix_sum[index]
            print sum
            if sum in hash:
                return [hash[sum]+1, index]
            else:
                hash[sum] = index

        return []
