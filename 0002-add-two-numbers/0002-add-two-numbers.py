# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # 1. Create a dummy head to start our new list
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # 2. Loop until everything is processed
        while l1 or l2 or carry:
            # Get values (use 0 if the list has ended)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            
            # 3. Create new node and move forward
            curr.next = ListNode(val)
            curr = curr.next
            
            # Move l1 and l2 forward if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        # 4. Return the list starting AFTER the dummy
        return dummy.next