# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # perform BFS

        #check if tree exists
        if not root:
            return None
        
        # queue root node into queue
        queue = deque([root])

        while queue:
            # node = pop the left of queue
            node = queue.popleft()
            # swap children of that node
            node.left, node.right = node.right, node.left
            #if left exists add to queue
            if node.left:
                queue.append(node.left)
            # if right exists add to queue
            if node.right:
                queue.append(node.right)

        return root