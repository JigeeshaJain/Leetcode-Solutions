"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtoCopy={None : None}
        
        curr=head
        while curr:
            copy=Node(curr.val)
            oldtoCopy[curr]=copy #using a hashmap we r mapping a old node to the copy node i.e. new node 
            curr=curr.next
            
        curr=head
        while curr:
            copy=oldtoCopy[curr]
            copy.next=oldtoCopy[curr.next]
            copy.random=oldtoCopy[curr.random]
            curr=curr.next
            
        return oldtoCopy[head]
            
            
        
        
        
        