# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currL1 = list1
        currL2 = list2
        output = ListNode()
        curr = output

        if not list1:
            return list2
        if not list2:
            return list1

        while currL1 and currL2:
            if currL1.val > currL2.val:
                curr.val = currL2.val
                currL2 = currL2.next
            elif currL1.val == currL2.val:
                curr.val = currL1.val
                curr.next = ListNode()
                curr = curr.next
                curr.val = currL2.val
                currL1 = currL1.next
                currL2 = currL2.next
            else:
                curr.val = currL1.val
                currL1 = currL1.next
            if currL1 or currL2:
                curr.next = ListNode()
                curr = curr.next

        while currL1:
            curr.val = currL1.val
            currL1 = currL1.next
            if currL1:
                curr.next = ListNode()
                curr = curr.next

        while currL2:
            curr.val = currL2.val
            currL2 = currL2.next
            if currL2:
                curr.next = ListNode()
                curr = curr.next
        


        return output