class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0 
        for i in range(len(nums)):
            if nums[i] == 1: 
                current_max = 1
                for j in range(i+1, len(nums)):
                    if nums[j] == 1: 
                        current_max += 1
                    else: 
                        break 
                if current_max > max_consecutive:
                    max_consecutive = current_max
        return max_consecutive