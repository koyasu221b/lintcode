class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        n = len(s1)
        m = len(s2)
        if n + m != len(s3):
            return False
        f = [[ False for j in range(m+1)] for i in range(n+1)]
        f[0][0] = True

        for i in range(1, n+1):
            if f[i-1][0] and s1[i-1] == s3[i-1]:
                f[i][0] = True

        for j in range(1, m+1):
            if f[0][j-1] and s2[j-1] == s3[j-1]:
                f[0][j] = True

        for i in range(1,n+1):
            for j in range(1, m+1):
                if f[i-1][j] and  s1[i-1] == s3[i+j-1]:
                    f[i][j] = True
                if f[i][j-1] and s2[j-1] == s3[i+j-1]:
                    f[i][j] = True

        return f[n][m]
