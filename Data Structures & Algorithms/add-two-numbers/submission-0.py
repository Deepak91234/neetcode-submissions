# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while first or second or carry:
            x = first.val if first else 0
            y = second.val if second else 0
            total = x + y + carry
            digit = total % 10
            carry = total // 10
            current.next = ListNode(digit)
            current = current.next
            if first:
                first = first.next
            if second:
                second = second.next
        return dummy.next