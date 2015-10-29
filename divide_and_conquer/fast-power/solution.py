class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b

        if n == 1:
            return a % b

        product = self.fastPower(a, b, n/2)
        if n % 2 == 0:
            return (product * product) % b
        else:
            return (product * product * a) % b
