class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix_T = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)): 
            for j in range(len(matrix[0])): 
                matrix_T[j][i] = matrix[i][j] 
                print(i,j, matrix[i][j], matrix_T[j][i]) 
        print(matrix_T) 
        return matrix_T 