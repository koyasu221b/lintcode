class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        n = len(A)
        if n == 0:
            return False
        f = [False for i in range(n)]
        f[0] = True
        for i in xrange(1, n):
            for j in xrange(0, i):
                if f[j] is True and (j + A[j]) >=i:
                    f[i] = True
                    break

        return f[n-1]
