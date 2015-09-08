class Solution:
    # @param s, a string
    # @return an integer

    def is_palindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1

        return True

    def get_is_palindrome(self, s):
        n = len(s)
        result = [[False for i in range(n)] for i in range(n)]
        for i in range(n):
            result[i][i] = True
        for i in range(n-1):
            result[i][i+1] = True if s[i] == s[i+1] else False

        for length in range(2, n):
            start = 0
            while start + length < n:
                result[start][start+length] = result[start+1][start+length-1] and (s[start] == s[start+length])
                start+=1

        return result


    def minCut(self, s):
        # write your code here
        n = len(s)
        if n == 0 or s is None:
            return 0

        f = [i-1 for i in range(n+1)]
        is_palindrome = self.get_is_palindrome(s)

        for cut_pos in range(1, n+1):
            for this_cut in range(0, cut_pos):
                start = this_cut
                end = cut_pos -1
                if is_palindrome[start][end]:
                    f[cut_pos] = min(f[cut_pos], f[this_cut]+1)

        return f[n]
