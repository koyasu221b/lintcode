class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 0 or n == 0 or obstacleGrid[0][0] == 1:
            return 0
        f = [[0 for i in range(n)] for i in range(m)]
        f[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                f[i][0] = 1
            else:
                break

        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                f[0][i] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    f[i][j] = f[i-1][j] + f[i][j-1]
                else:
                    f[i][j] = 0

        return f[m-1][n-1]

