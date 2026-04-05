# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head
        #cant move right into position without a loop directly sooo
        while n > 0 and right:
            right = right.next
            n -= 1
        #now right is in position
        while right:
            left = left.next
            right = right.next # made a very stupid typo here hahah
        #delete the node
        left.next = left.next.next
        return dummy.next