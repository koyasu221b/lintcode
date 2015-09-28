class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        result = []
        sub_result = []
        sorted_S = sorted(list(S))
        self.subsets_helper(result, sub_result, sorted_S, 0)
        return result

    def subsets_helper(self, result, sub_result, sorted_S, position):

        result.append(list(sub_result))
        for index in range(position, len(sorted_S)):
            sub_result.append(sorted_S[index])
            self.subsets_helper(result, sub_result, sorted_S, index+1)
            sub_result.pop()
