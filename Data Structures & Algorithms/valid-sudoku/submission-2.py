class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i, j = 0, 0
        size = len(board)
        row = {index: set() for index in range(size)}
        col = {index: set() for index in range(size)}
        sqr = {index: set() for index in range(size)}
        while i < size:
            while j < size:
                square = self.whichSquare(i, j)
                if board[i][j] == '.':
                    j+=1
                    continue
                if board[i][j] in sqr[square]:
                    return False
                else:
                    sqr[square].add(board[i][j])
                if board[i][j] in col[i]:
                    return False
                else:
                    col[i].add(board[i][j])
                if board[i][j] in row[j]:
                    return False
                else:
                    row[j].add(board[i][j])
                j+=1
            j = 0
            i+=1

        return True
    
    def whichSquare (self, i, j):
        return (i // 3) * 3 + (j // 3)