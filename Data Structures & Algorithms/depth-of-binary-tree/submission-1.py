# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       #iterative  BFS 
        if not root:
            return 0
        q = deque([root])
        level = 0
        while q:
            qlen = len(q)
            for i in range(qlen):#level incrementation should be out sid efor loop since then it increaments for each level not each node
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level

            