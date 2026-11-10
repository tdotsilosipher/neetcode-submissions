# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # keep track of levels
        level = 0

        #if no root no tree level = 0
        if not root:
            return level
        #if root exists add to q
        q = deque([root])
        
        #BFS, while queue exists
        while q:
            # only iterate each level to track levels instead of nodes
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
        