# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        l1 = head
        l2 = slow.next
        slow.next = None

        prev = None

        while l2:
            nxt = l2.next
            l2.next = prev
            prev = l2
            l2 = nxt

        l2 = prev

        while l2:
            next_l1 = l1.next
            next_l2 = l2.next

            l1.next = l2
            l2.next = next_l1

            l1 = next_l1
            l2 = next_l2

        return