# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:  
        first = 0
        last = n   
        mid = (first + last) // 2   
        while guess(mid) != 0:
            if guess(mid) == -1: 
                last = mid - 1
            else: 
                first = mid + 1
            mid = (first + last) // 2
        
        return mid

