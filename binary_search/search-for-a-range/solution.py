class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # left-bound: find target's first position
        if len(A) == 0:
            return [-1, -1]
        start ,end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if A[mid] == target:
                end = mid
            elif A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid

        if A[start] == target:
            left_bound  = start
        elif A[end] == target:
            left_bound = end
        else:
            left_bound = -1

        # right-bound: find target's last position
        start ,end = 0, len(A) -1
        while start + 1 < end:
            mid = start + (end - start)/2
            if A[mid] == target:
                start = mid
            elif A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
        if A[end] == target:
            right_bound = end
        elif A[start] == target:
            right_bound = start
        else:
            right_bound = -1
        return [left_bound, right_bound]
