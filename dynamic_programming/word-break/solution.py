class Solution:
    def get_max_word_length(self, _dict):
        if len(_dict) == 0:
            return 0
        max_word_length = 0
        for i in _dict:
            max_word_length  = max(max_word_length, len(i))
        return max_word_length

    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        n = len(s)
        if n==0:
            return True
        max_word_length = self.get_max_word_length(dict)
        print "max_word_length", max_word_length
        f = [False for i in range(n+1)]
        f[0] = True
        for i in range(1, n+1):
            last_word_length = 1
            while last_word_length <= max_word_length and last_word_length <=i:
                index = i - last_word_length
                if f[index] and s[index:i] in dict:
                    f[i] = True
                    break
                last_word_length +=1
        return f[n]
