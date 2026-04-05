# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(Node,maxvalue):
            if not Node:
                return 0
                #base case
            res = 1 if Node.val >= maxvalue else 0 #good if greater or equal to max
            maxvalue =max(maxvalue,Node.val) #update max
            res += dfs(Node.left,maxvalue) #recursivly call on left and right
            res += dfs(Node.right,maxvalue)
            return res # final return
        return dfs(root,root.val)