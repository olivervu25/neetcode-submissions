# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque() 
        output = []

        if root: 
            queue.append(root)
        else: 
            return [] 
        


        while len(queue) > 0: 

            current_row = []

            for i in range(len(queue)): 

                curr = queue.popleft() 

                current_row.append(curr.val)

                if curr.left: 
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
           
            output.append(current_row) 
        
        return output 
            




        