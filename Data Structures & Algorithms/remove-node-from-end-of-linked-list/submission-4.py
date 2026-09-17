# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        for i in range(n):
            first = first.next
        if not first:
            return head.next
        second = head
        prev = None
        while first:
            prev = second
            second = second.next
            first = first.next
        
        prev.next = second.next
        return head