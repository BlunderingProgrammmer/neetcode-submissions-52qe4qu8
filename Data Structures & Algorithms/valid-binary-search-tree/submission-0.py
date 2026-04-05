# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid_Node(Node,left,right):
            #also empty BST also valid
            if not Node:
                return True
                #make a not comparision
            if not (Node.val > left and Node.val < right):
                return False
                #call recursively for left and right
            return (valid_Node(Node.left,left,Node.val) and valid_Node(Node.right,Node.val,right))
#call with def values
        return valid_Node(root,float('-inf'),float('inf'))