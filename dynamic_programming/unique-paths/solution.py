class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        f = [[0 for x in range(n)] for x in range(m)]
        f[0][0] = 1
        for i in range(1, m):
            f[i][0] = 1
        for i in range(1, n):
            f[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i-1][j] + f[i][j-1]

        return f[m-1][n-1]
