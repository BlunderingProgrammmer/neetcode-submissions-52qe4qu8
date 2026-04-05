"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # a basic hashmap to map old nodes -> new nodes 
        old_to_new = {}
        #define a dfs function 
        def dfs(node):
            if node in old_to_new: #checking if node already has a copy check using hashmap..return the copy node so u can add it to 
            #neighbors list
                return old_to_new[node]
            
            copy = Node(node.val) # if doesnt exitst then create a node copy 
            old_to_new[node] = copy #create  map the new copy to its old in hashmap
            #create the nei list
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei)) # since dfs base is return old to new append that to the copy ka nei list
            return copy # return any node
        return dfs(node) if node else None # edge case if node is empty