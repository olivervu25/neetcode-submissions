class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0 
        R = len(nums) - 1
        M = (R+L)//2 

        if nums[L] == target: 
            return L
        if nums[R] == target: 
            return R

        while nums[M] != target and L != M: 
            if nums[M] > target: 
                R = M 
                M = (L + R)//2
            else: 
                L = M 
                M = (L + R) // 2
    
        if nums[M] == target: 
            return M 
        else: 
            return -1