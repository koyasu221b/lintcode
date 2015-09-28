class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        result = []
        sub_result = []
        sorted_s = sorted(list(S))
        self.subsets_helper(result, sub_result, sorted_s, 0)
        return result

    def subsets_helper(self, result, sub_result, sorted_s, pos):
        result.append(list(sub_result))
        for index in range(pos, len(sorted_s)):
            if pos!=index and sorted_s[index] == sorted_s[index-1]:
                continue
            sub_result.append(sorted_s[index])
            self.subsets_helper(result, sub_result, sorted_s, index+1)
            sub_result.pop()
