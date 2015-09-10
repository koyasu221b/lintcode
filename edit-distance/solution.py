class Solution:
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        import sys
        # write your code here
        m = len(word1)
        n = len(word2)

        f = [[sys.maxint for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            f[i][0] = i

        for j in range(n+1):
            f[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i][j-1], f[i-1][j], f[i-1][j-1]) +1

        return f[m][n]
