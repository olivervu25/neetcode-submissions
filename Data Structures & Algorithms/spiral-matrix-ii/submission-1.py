class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0
        matrix = [[0] * n for _ in range(n)]
        x, y = 0,0 
        dx, dy = directions[d][0], directions[d][1]
        visitted = set() 

        for i in range(1, n**2 + 1): 
            matrix[x][y] = i
            visitted.add((x,y)) 
            if x + dx < 0 or y + dy < 0 or x + dx > n - 1 or y + dy > n - 1 or (x + dx, y + dy) in visitted: 
                d = (d + 1) % 4
                dx, dy = directions[d][0], directions[d][1]
            x, y = x + dx,y + dy 
        
        return matrix 
