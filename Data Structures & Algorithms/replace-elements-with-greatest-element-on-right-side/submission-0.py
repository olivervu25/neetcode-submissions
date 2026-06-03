class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_list = []
        for i in range(len(arr)-1): 
            max_list.append(max(arr[i+1:len(arr)]))
        max_list.append(-1)
        return max_list