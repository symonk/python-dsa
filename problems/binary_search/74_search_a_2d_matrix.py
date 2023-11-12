class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid]
            row_res = False
            row_l, row_r = 0, len(val) - 1
            while row_l <= row_r:
                row_mid = (row_l + row_r) // 2
                row_val = val[row_mid]
                if row_val == target:
                    row_res = True
                    break
                if row_val > target:
                    row_r = row_mid - 1
                else:
                    row_l = row_mid + 1
            if row_res is True:
                return True
            if val[0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
