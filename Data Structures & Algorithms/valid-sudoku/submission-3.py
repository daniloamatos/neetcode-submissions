class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        row = {index: set() for index in range(size)}
        col = {index: set() for index in range(size)}
        sqr = {index: set() for index in range(size)}
        for i in range(size):
             for j in range(size):
                value = board[i][j]
                square = self.whichSquare(i, j)
                if value == '.':
                    continue
                elif value in sqr[square]:
                    return False
                elif value in col[i]:
                    return False
                elif value in row[j]:
                    return False
                sqr[square].add(value)
                col[i].add(value)
                row[j].add(value)
        return True
    
    def whichSquare (self, i, j):
        return (i // 3) * 3 + (j // 3)