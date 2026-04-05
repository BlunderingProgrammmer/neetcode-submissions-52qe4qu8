# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #use recursion to invert tree and traverse using DFS
        if not root:
            return None
        #swap the children in this block
        tmp = root.right
        root.right = root.left
        root.left = tmp
        #recursive call inside the function
        self.invertTree(root.left)
        self.invertTree(root.right)
        #clean up based on base case
        return root