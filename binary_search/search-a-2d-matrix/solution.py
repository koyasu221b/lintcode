class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):

        rows = len(matrix)
        if rows == 0:
            return False
        columns = len(matrix[0])


        # find the row index, the last number <= target
        start, end = 0, rows -1
        while start + 1 < end:
            mid = start + (end - start)/2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end = mid
            elif matrix[mid][0] < target:
                start = mid

        if matrix[end][0] <= target:
            row = end
        elif matrix[start][0] <= target:
            row = start
        else:
            return False

        # find the column index
        start, end = 0, columns -1
        while start + 1 < end:
            mid = start + (end - start)/2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid
            elif matrix[row][mid] < target:
                start = mid

        if matrix[row][start] == target:
            return True
        if matrix[row][end] == target:
            return True

        return False

