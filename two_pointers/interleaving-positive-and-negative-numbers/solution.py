class Solution:
    """
    @param A: An integer array.
    @return nothing
    """
    def rerange(self, A):
        # write your code here
        positive_count = 0
        negative_count = 0
        for number in A:
            if number < 0:
                negative_count+=1
            else:
                positive_count+=1

        is_positive_first = True if positive_count > negative_count else False

        left = 0
        right = len(A)-1
        while left <= right:
            while left <= right and not self.is_swap(A[left],is_positive_first):
                left+=1
            while left <= right and self.is_swap(A[right],is_positive_first):
                right-=1
            if left <= right:
                A[left], A[right] = A[right] , A[left]
                left+=1
                right-=1

        n = len(A)
        for index in range(n):
            if is_positive_first and A[index] < 0:
                right = index
                break
            elif not is_positive_first and A[index] >=0:
                right = index
                break

        for i in range(1, n, 2):
            if right < n:
                A[i], A[right] = A[right], A[i]
                right+=1

    def is_swap(self, value, flag):
        if flag:
            return True if value < 0 else False
        else:
            return True if value > 0 else False



    def is_swap_2(self, position):
        if position % 2 != 0:
            return True
        else:
            return False
