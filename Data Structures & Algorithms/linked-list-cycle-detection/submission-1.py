# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_dict = {} 
        curr = head 
        i = 0
        count = 0
        if not head: 
            return False 
        while curr.next : 
            if curr.next.val in my_dict:
                i = my_dict[curr.next.val] 
                curr = curr.next 
                count += 1
            else: 
                my_dict[curr.val] = i
                i += 1 
                curr = curr.next 

            if count == 2: 
                return True 
        return False 