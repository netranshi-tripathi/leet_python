# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        prev=None
        curr=head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        head=prev
        return head
    def printLL(self,heaad):
        
        curr=head
        l=[]
        if head==None:
            print(l)
        while curr:
            l.append(curr.val)
            curr=curr.next
        print(l)

        

        