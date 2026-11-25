"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned = {}
        # make copy of node value
        cloned[node] = Node(node.val)
        # put node into q
        q = deque([node])

        while q:
            ptr = q.popleft()
            for i in ptr.neighbors:
                if i not in cloned:
                    cloned[i] = Node(i.val)
                    q.append(i)
                cloned[ptr].neighbors.append(cloned[i])
        return cloned[node]


