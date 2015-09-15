class Solution:
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        m = len(S)
        n = len(T)

        f = [[0 for i in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            f[i][0] = 1

        for j in range(1, n+1):
            f[0][j] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                print i, j , S[i-1], T[j-1]
                if S[i-1] == T[j-1]:
                    print f[i-1][j-1]
                    f[i][j] = f[i-1][j-1] + f[i-1][j]
                else:
                    f[i][j] = f[i-1][j]

        return f[m][n]
