# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque() 
        output = []
        if root: 
            queue.append(root) 
        else: 
            return []

        level = 0 
        while len(queue) > 0: 
            output.append(queue[-1].val) 
            for i in range(len(queue)): 
                curr = queue.popleft() 

                if curr.left: 
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
        
        return output 



        