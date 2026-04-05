# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #carefull with the base case here 
        if not subRoot:
            return True
        if not root:
            return False
        #use helper function
        if self.issametree(root,subRoot):
            return True
            #compare with root left and right to whole subtreeand return true is any true
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

    def issametree(self,root,subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.issametree(root.left,subRoot.left) and 
                self.issametree(root.right,subRoot.right))
        return False