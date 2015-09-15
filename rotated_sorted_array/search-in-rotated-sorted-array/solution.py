class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        if len(A) == 0:
            return -1
        start, end = 0, len(A)-1
        compare = A[end]
        while start + 1 < end:
            mid = start + (end - start)/2
            if A[mid] > compare:
                start = mid
            elif A[mid] == compare:
                end = mid
            elif A[mid] < compare:
                end = mid

        if A[start] < A[end]:
            min_pos = start
        else:
            min_pos = end

        start, end = 0, len(A)-1
        if target >= A[min_pos] and target <= A[end]:
            start = min_pos
        else:
            end = min_pos -1

        while start+1 < end:
            mid = start + (end - start)/2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
