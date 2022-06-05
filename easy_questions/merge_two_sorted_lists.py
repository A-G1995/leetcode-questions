# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        current = head
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            
            current = current.next
            
        if l1 != None:
            current.next = l1
        
        if l2 != None:
            current.next = l2
        
        return head.next
        
print(mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))))