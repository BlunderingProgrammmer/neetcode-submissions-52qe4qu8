# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #use recursive solution
        if not head:
            return None #base case for recursivce calll
        head_of_reversed_list = head #our job is to dig deep and grab the last node
        if head.next:#if head.next exist then it means we are not yet at the last node
            head_of_reversed_list = self.reverseList(head.next)#recursive dig
            head.next.next = head#reverse link 
            head.next = None#clean up line
        return head_of_reversed_list #return head