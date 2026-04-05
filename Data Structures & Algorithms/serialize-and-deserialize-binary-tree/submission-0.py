# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = [] # use a join later to convert to a string
        def dfs(root):
            if not root:
                res.append("N")
                return 
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return ",".join(res)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        array_of_nodes = data.split(",")
        self.i = 0# member poiter to be kept track of array when traversing globally

        def dfs():
            data_point = array_of_nodes[self.i]
            if data_point == "N":
                self.i +=1
                return None
            Node = TreeNode(int(data_point))
            self.i +=1
            Node.left = dfs()
            Node.right = dfs()
            return Node
        return dfs()
            