class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])

        l = 0
        r = height * width

        while l < r:
            m = (l + r) // 2
            cur = matrix[m // width][m % width]
            if target == cur:
                return True
            elif target < cur:
                r = m
            else:
                l = m + 1

        return False
        