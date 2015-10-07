class Solution:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        # write your code here
        result = []
        sub_result = []
        candidates = sorted(candidates)
        self.helper(result, sub_result, 0, candidates, target)
        return result


    def helper(self, result, sub_result, start_index, candidates, target):
        if target == 0:
            result.append(list(sub_result))
            return
        previous = -1
        for index in range(start_index, len(candidates)):
            current = candidates[index]
            if current > target:
                return
            if start_index!=index and current==candidates[index-1]:
                continue
            sub_result.append(current)
            self.helper(result, sub_result, index+1, candidates, target-current)
            sub_result.pop()
