class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        self.mergeSort(nums1[:m], 0, m-1)
        self.mergeSort(nums2[:n], 0, n)

        nums1[m:] = nums2

        return self.sort(nums1, 0, m+n - 1, m-1)        
        

    def mergeSort(self, arr, s, e): 
        if e - s + 1 <=1: 
            return arr
        
        m = (e + s) // 2
        
        self.mergeSort(arr, s, m)
        
        self.mergeSort(arr, m+1, e) 

        self.sort(arr, s, e, m) 

        return arr

    def sort(self, arr, s, e, m): 
        L = arr[s:m+1]
        R = arr[m+1:e+1]

        i = 0
        j = 0
        k = s

        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i]
                i += 1
            else: 
                arr[k] = R[j]
                j +=1 
            k += 1

        while i < len(L): 
            arr[k] = L[i]
            i+=1
            k+=1
        
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1 
        
        return arr
