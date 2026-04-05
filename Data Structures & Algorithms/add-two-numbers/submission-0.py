# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry: # add carry statement here so that if only carry remains still add it and create val andnew node in res list
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry

            # calc carry
            carry = val // 10
            val = val % 10
            #insert into new linked list
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return dummy.next 

