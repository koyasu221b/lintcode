class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums is None:
            return []
        result = []
        sub_result = []
        self.helper(result, sub_result, nums)
        return result

    def helper(self, result, sub_result, nums):
        if len(sub_result) == len(nums):
            result.append(list(sub_result))

        for i in range(len(nums)):
            if nums[i] in sub_result:
                continue
            sub_result.append(nums[i])
            self.helper(result, sub_result, nums)
            sub_result.pop()
