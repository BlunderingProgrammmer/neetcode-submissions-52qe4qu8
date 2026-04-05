# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] #list cuz its easier to dynamically update 

        def dfs(root):
            if not root:
                return 0

            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            #maximum with the split in part of the tree
            #dont need to include if neg value during split in the res update
            leftmax = max(leftmax,0)
            rightmax = max(rightmax,0)
            res[0] = max(res[0],root.val+leftmax+rightmax)
            # what u are returning is the individuall path for both
            return root.val + max(leftmax,rightmax)

        dfs(root)
        return res[0]