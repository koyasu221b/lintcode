class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0

        f = [0 for x in range(n)]
        f[0] = 1
        max_sub_seq = 0
        for i in range(0, n):
            for j in range(0, i):
                if nums[i]>=nums[j]:
                    f[i] = max(f[j] + 1, f[i])
                else:
                    f[i] = max(f[i], 1)
            max_sub_seq = max(max_sub_seq, f[i])

        return max_sub_seq
