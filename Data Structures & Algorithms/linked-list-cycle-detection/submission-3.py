# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set = set() 
        curr = head 
        my_set.add(curr) 
        if not curr: 
            return False 
        while curr.next: 
            if curr.next in my_set:
                return True 
            else: 
                my_set.add(curr) 
                curr = curr.next 

        return False  