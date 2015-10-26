class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n == 0:
            return False
        if (n-1) & n == 0:
            return True
        return False
