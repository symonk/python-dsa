class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid]
            if target in val:
                return True
            if val[0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
