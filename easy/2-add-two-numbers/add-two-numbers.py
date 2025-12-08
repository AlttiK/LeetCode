# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        curr = ans
        carry = 0

        while l1 is not None or l2 is not None or carry > 0:
            digit1 = 0
            digit2 = 0
            if l1 is not None:
                digit1 = l1.val
            if l2 is not None:
                digit2 = l2.val
            
            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10
            curr.next = ListNode(digit)
            curr = curr.next

            if l1 is not None: 
                l1 = l1.next
            if l2 is not None: 
                l2 = l2.next
        solution = ans.next
        ans.next = None
        return solution
        
        
        