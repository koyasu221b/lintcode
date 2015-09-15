ass Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        start , end = 1, len(A)-2

        while start + 1 < end:
            mid = start + (end - start)/2
            #case 1 : increase interval
            if A[mid] > A[mid-1] and A[mid] < A[mid+1]:
                start = mid
            #case 2 : decrease interval
            elif A[mid] < A[mid-1] and A[mid] > A[mid+1]:
                end = mid
            #case 3: peak
            elif A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            #case 4: bottom
            elif A[mid] < A[mid-1] and A[mid] < A[mid+1]:
                end = mid

        if A[start] < A[end]:
            return end
        return start
