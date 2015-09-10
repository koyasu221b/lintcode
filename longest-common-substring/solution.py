class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        f = [[0 for j in range(n+1)] for i in range(m+1)]

        for j in range(n+1):
            f[0][j] = 0
        for i in range(m+1):
            f[i][0] = 0
        max_length = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    f[i][j] = f[i-1][j-1] +1
                    if f[i][j] > max_length:
                        max_length = f[i][j]
                else:
                    f[i][j] = 0

        return max_length

