class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        letters = list(chars)
        left = 0
        right = len(letters)-1
        while left <= right:
            while left <= right and letters[left].islower():
                left+=1
            while left <= right and (not letters[right].islower()):
                right-=1
            if left <= right:
                letters[left], letters[right] = letters[right], letters[left]

        return ''.join(letters)
