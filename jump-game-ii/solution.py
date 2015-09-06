import sys
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        n = len(A)
        f = [sys.maxint for i in range(n)]
        f[0] = 0
        for i in range(1, n):
            for j in range(0, i):
                if A[j] + j >= i and f[j]!= sys.maxint:
                    f[i] = f[j] + 1
                    break

        return f[n-1]
