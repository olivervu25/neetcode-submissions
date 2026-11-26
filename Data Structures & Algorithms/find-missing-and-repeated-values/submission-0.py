class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums = set(range(1, len(grid)**2 + 1))
        output = [0,0]
        for row in grid: 
            for num in row: 
                if num in nums: 
                    nums.remove(num) 
                else:
                    output[0] = num
        output[1] = nums.pop() 

        return output
