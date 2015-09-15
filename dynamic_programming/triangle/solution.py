import sys
class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        n = len(triangle)
        if n == 0:
            return 0
        f = [[sys.maxint for x in range(n)] for x in range(n)]
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(0, i+1):
                f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i][j]
                print i,j, f[i][j]

        min_sum = f[n-1][0]
        for i in range(1, n):
            min_sum = min(min_sum, f[n-1][i])

        return min_sum
