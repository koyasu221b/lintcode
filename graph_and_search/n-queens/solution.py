class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        result = []
        sub_result = []
        self.search(result, sub_result, n)
        return result

    def search(self, result, sub_result, n):
        if len(sub_result) == n:
            result.append(self.draw_chess_board(sub_result))
            return

        for col in range(n):
            if not self.is_valid(sub_result, col):
                continue
            sub_result.append(col)
            self.search(result,sub_result, n)
            sub_result.pop()

    def is_valid(self, sub_result, col):
        rows = len(sub_result)
        for current_row in range(rows):
            current_col = sub_result[current_row]
            if current_col == col:
                return False
            if current_row - current_col == rows - col:
                return False
            if current_row + current_col == rows + col:
                return False

        return True



    def draw_chess_board(self, sub_result):
        chess_board = []
        for row in range(len(sub_result)):
            result = ''
            for col in range(len(sub_result)):
                if sub_result[row] == col:
                    result += 'Q'
                else:
                    result += '.'
            chess_board.append(result)
        return chess_board

