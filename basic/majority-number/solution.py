class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        majority_number = nums[0]
        count = 1
        for index in range(1, len(nums)):
            if nums[index] == majority_number:
                count+=1
            else:
                count-=1

            if count == 0:
                majority_number = nums[index]
                count = 1

        return majority_number
