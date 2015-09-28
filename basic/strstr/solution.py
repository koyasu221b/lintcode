class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        if len(source) == 0 and len(target) == 0:
            return 0
        elif len(target) == 0:
            return 0
        for s in range(len(source)):
            for t in range(len(target)):
                if source[s+t] != target[t]:
                    break
                if t == len(target)-1:
                    return s

        return -1

