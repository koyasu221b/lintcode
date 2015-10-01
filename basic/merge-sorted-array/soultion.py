class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        current = m+n -1
        i = m -1
        j = n -1
        while i >=0 and j>=0:
            if A[i] > B[j]:
                A[current] = A[i]
                i-=1
            else:
                A[current] = B[j]
                j-=1
            current -=1
        while i>=0:
            A[current] = A[i]
            current -=1
            i-=1
        while j>=0:
            A[current] = B[j]
            current -=1
            j-=1
