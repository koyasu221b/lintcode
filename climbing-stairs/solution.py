class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        f = [0, 1, 2]
        if n <= 2:
            return f[n]

        for i in range(3, n+1):
            f.append(f[i-1] + f[i-2])

        return f[n]
