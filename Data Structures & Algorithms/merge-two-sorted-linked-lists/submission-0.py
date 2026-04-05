# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #empty placeholder 
        tail = dummy #creating  a pointer that points to the empty node...like a train coupler

        while list1 and list2:#checking if both lists are non empty
            if list1.val < list2.val:
                tail.next = list1 #coupler linked to list1
                list1 = list1.next#move to next one
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next #move the coupler so u can add more later without losing what we had
        if not list1:
            tail.next = list2
        elif not list2:
            tail.next = list1
        return dummy.next