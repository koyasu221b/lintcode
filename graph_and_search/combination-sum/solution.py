class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = sorted(candidates)
        result = []
        sub_result = []
        self.helper(candidates, result, sub_result, 0, target)
        return result

    def helper(self, candidates, result, sub_result, start_index, target):
        if target == 0:
            result.append(list(sub_result))
            return

        for index in range(start_index, len(candidates)):
            current = candidates[index]
            if current > target:
                return
            sub_result.append(current)
            self.helper(candidates, result, sub_result, index, target - current)
            sub_result.pop()
