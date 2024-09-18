# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            if fast.next and fast.next.next:
                fast=fast.next.next
            else:
                fast=fast.next
        if slow.next:
            slow.val=slow.next.val
            slow.next=slow.next.next
        else:
            head.next=None
        return head