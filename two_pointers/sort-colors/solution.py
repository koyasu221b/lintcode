class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        next_start_index = self.sort_color_helper(0, 0, nums)
        self.sort_color_helper(next_start_index, 1, nums)


    def sort_color_helper(self, start_index, sort_color, nums):
        left = start_index
        right = len(nums)-1
        while left <= right:
            while left <= right and nums[left] == sort_color:
                left+=1
            while left <= right and nums[right] != sort_color:
                right-=1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
        return left
