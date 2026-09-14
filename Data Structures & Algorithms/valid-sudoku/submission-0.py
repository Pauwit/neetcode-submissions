class Solution:
    def convertBoard(self, board: List[List[str]]) -> List[List[int]]:
        ret = [[0] * 9] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                ret[i][j] = int(board[i][j])

        return ret

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #board = self.convertBoard(board)
        print(board)

        columns = [[False for _ in range(9)] for _ in range(9)]
        rows = [[False for _ in range(9)] for _ in range(9)]
        boxes = [[[False for _ in range(9)] for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    continue
                cur = int(board[row][column]) - 1
                
                if columns[column][cur] or rows[row][cur] or boxes[row // 3][column // 3][cur]:
                    return False
                
                columns[column][cur] = True
                rows[row][cur] = True
                boxes[row // 3][column // 3][cur] = True

        return True