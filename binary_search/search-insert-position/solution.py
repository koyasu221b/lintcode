class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        if len(A) == 0:
            return 0
        # find the first position >= target
        start, end = 0, len(A) -1
        while start + 1 < end:
            mid = start + (end - start)/2
            if A[mid] == target:
                end = mid
            elif A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
        if A[start] >= target:
            return start
        elif A[end] >= target:
            return end
        else:
            return end + 1
