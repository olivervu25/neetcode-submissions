class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = {")": "(", "}": "{", "]": "["}
        for element in s:
            if element in "({[": 
                stack.append(element)
            else: 
                if len(stack) == 0: return False
                if stack.pop() != bracket_dict[element]:
                    return False 
        if len(stack) == 0: 
            return True
        else: 
            return False 