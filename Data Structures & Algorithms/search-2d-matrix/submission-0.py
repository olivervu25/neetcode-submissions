class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1 

        while left <= right: 
            mid = (left + right) // 2

            if matrix[mid][0] > target: 
                right = mid - 1
            elif matrix[mid][-1] < target: 
                left = mid + 1
            else: 
                L = 0
                R = len(matrix[mid]) - 1

                while (L <= R): 
                    M = (L + R) // 2
                    if matrix[mid][M] > target: 
                        R = M - 1
                    elif matrix[mid][M] < target: 
                        L = M + 1
                    else: 
                        return True
                
                return False 
            
        return False 
                        
 