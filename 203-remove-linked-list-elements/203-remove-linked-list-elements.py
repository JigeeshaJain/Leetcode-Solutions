# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        prev,curr=dummy,head
        
        while curr:
            nxt=curr.next
            
            if curr.val==val:
                prev.next=nxt
                
            else:
                prev=curr #here we r just shifting the prev pointer and not updating the previous val as there is no such need. And we r shifting as we need to point the value of prev.next to curr whenever curr.val=val. So we r simply updating the prev value
            
            curr=nxt
            
        return dummy.next
        