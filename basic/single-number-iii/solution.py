class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """
    def singleNumberIII(self, A):
        # write your code here
        xor_sum = 0
        for number in A:
            xor_sum^=number

        last_1_bit = xor_sum - (xor_sum & xor_sum-1)
        group_0 = 0
        group_1 = 0

        for number in A:
            if (number & last_1_bit) == 0:
                group_0 ^= number
            else:
                group_1 ^= number

        return group_0, group_1

