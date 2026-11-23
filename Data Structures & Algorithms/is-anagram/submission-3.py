class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}  
        if len(t) != len(s): 
            return False 
        for i in range(len(s)): 
            if s[i] in dict_t and dict_t[s[i]] > 0: 
                dict_t[s[i]] -= 1
            else: 
                if s[i] in dict_s: 
                    dict_s[s[i]] += 1
                else: 
                    dict_s[s[i]] = 1
            
            if t[i] in dict_s and dict_s[t[i]] > 0: 
                dict_s[t[i]] -= 1
            else: 
                if t[i] in dict_t: 
                    dict_t[t[i]] += 1
                else: 
                    dict_t[t[i]] = 1
        print(dict_s)
        print(dict_t) 
        return True if sum(value for value in dict_s.values()) == 0 and sum(value for value in dict_t.values()) == 0 else False 