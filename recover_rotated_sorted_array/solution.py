class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        for index in range(len(nums)-1):
            if nums[index] > nums[index+1]:
                self.reverse(nums, 0, index)
                self.reverse(nums, index+1, len(nums)-1)
                self.reverse(nums, 0, len(nums)-1)


    def reverse(self, nums, start, end):
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start +=1
            end -=1

