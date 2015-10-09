class Solution:
    """
        @param A : An integer array
        @return : An integer
    """
    def singleNumberII(self, A):
        # write your code here
        pow_of_3s = []
        total = 20
        tmp = 1
        for i in range(total):
            pow_of_3s.append(tmp)
            tmp *=3

        bits = [0 for i in range(total)]
        for i in range(total):
            for each_number in A:
                bits[i] += (each_number/pow_of_3s[i] ) %3

        result = 0
        for i in range(total):
            result += (bits[i]%3)*pow_of_3s[i]

        return result
