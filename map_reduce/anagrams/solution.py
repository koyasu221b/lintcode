class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        count = {}
        for str in strs:
            list_str = list(str)
            if len(list_str) == 0:
                list_str = ['']
            sorted_str = ''.join(sorted(list_str))
            if sorted_str in count:
                count[sorted_str]+=1
            else:
                count[sorted_str] = 1

        result = []
        for str in strs:
            sorted_str = ''.join(sorted(list(str)))
            if count[sorted_str] >1:
                result.append(str)

        return result
