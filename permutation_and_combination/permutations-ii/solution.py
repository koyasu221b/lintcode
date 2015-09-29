class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        result = []
        sub_result = []
        visited = [False for i in range(len(nums))]
        sorted_nums = sorted(nums)
        self.helper(result, sub_result, visited, sorted_nums)
        return result

    def helper(self, result, sub_result, visited, sorted_nums):
        if len(sub_result) == len(sorted_nums):
            result.append(list(sub_result))
            return

        for index in range(len(sorted_nums)):
            if visited[index]:
                continue
            if index!=0 and not visited[index-1] and sorted_nums[index-1] == sorted_nums[index]:
                continue
            sub_result.append(sorted_nums[index])
            visited[index] = True
            self.helper(result, sub_result, visited, sorted_nums)
            sub_result.pop()
            visited[index] = False
