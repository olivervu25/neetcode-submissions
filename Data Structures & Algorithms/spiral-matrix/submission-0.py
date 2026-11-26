class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [(0,1), (1,0), (0,-1), (-1,0), ]
        d = 0
        dx, dy = direction[d] 
        lim_x, lim_y = len(matrix), len(matrix[0])
        output = []
        x, y = 0,0 
        visitted = set() 
        while len(output) < len(matrix) * len(matrix[0]): 
            output.append(matrix[x][y])
            visitted.add((x,y))
            if x + dx < 0 or x + dx > lim_x - 1 or y + dy < 0 or y + dy > lim_y - 1 or (x + dx, y + dy) in visitted: 
                d = (d + 1) % 4
            dx, dy = direction[d] 
            x, y = x + dx, y + dy 

        return output


            


        