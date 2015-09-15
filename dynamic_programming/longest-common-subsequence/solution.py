class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        m = len(B)
        n = len(A)
        f = [[0 for j in range(n+1)] for i in range(m+1)]

        for j in range(0, n+1):
           f[0][j] = 0

        for i in range(0, m+1):
            f[i][0] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if B[i-1] != A[j-1]:
                    f[i][j] = max(f[i][j-1], f[i-1][j])
                else:
                    f[i][j] = f[i-1][j-1] + 1

        return f[m][n]
