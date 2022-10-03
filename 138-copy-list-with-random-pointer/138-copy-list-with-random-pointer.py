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
        
        
        # we r using 2 passes i.e. 2 loops: 1st just creating/cloning old nodes to the hashmap and 2nd connecting the pointers  using the copy node created using hashmap 
        curr=head
        while curr:
            copy=Node(curr.val)
            oldtoCopy[curr]=copy #using a hashmap we r mapping a old node to the copy node i.e. new node 
            curr=curr.next
            
        curr=head
        while curr:
            copy=oldtoCopy[curr]  #to get the copy of our node accessing it using hashmap in order to set the pinters 
            copy.next=oldtoCopy[curr.next]
            copy.random=oldtoCopy[curr.random]
            curr=curr.next
            
        return oldtoCopy[head]
            
            
        
        
        
        