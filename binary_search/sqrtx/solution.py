class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        start = 1
        end = x
        while start+1 < end:
            mid = start + (end - start)/2
            product = mid * mid
            if product == x:
                return mid
            elif product < x:
                start = mid
            elif product > x:
                end = mid

        if start*start <= x:
            return start
        return end
