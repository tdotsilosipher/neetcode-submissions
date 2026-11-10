# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        #check if root does not exist
        if not root:
            return 0
        #instantiate queue BFS
        q = deque([root])
        
        while q:
            #for each node in current level
            for i in range(len(q)):
                node = q.popleft()
                #if left node not null
                if node.left:
                    q.append(node.left)
                #if right node not null
                if node.right:
                    q.append(node.right)
            # increment at each level
            level += 1
        return level