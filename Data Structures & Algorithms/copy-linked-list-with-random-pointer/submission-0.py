"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #create a hash map to store old node to copy node
        old_to_new = {None : None}
        curr = head
        # put all nodes to hash map
        while curr:
            copy = Node(curr.val)
            old_to_new[curr] = copy
            curr = curr.next
        # now create a  deep copy using the hashmap
        curr = head
        while curr:
            new_copy = old_to_new[curr]
            new_copy.next = old_to_new[curr.next]
            new_copy.random = old_to_new[curr.random]
            curr = curr.next
        return old_to_new[head] #pass the addresss of the new head
