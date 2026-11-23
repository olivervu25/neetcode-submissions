class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        
        count = {}

        for a, b in zip(s,t): 
            count[a] = count.get(a, 0) + 1 
            count[b] = count.get(b, 0) - 1

        print(count) 
        
        return all(value == 0 for value in count.values())