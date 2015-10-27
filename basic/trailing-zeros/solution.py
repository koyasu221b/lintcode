class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        sum = 0
        while n!=0:
            sum+= n/5
            n = n/5
        return sum
