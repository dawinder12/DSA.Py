class Node :
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
    def insertAtPos(head, p, x): # insert at pos after P
        # Code Here
        if not head :
            return None
        curr = head
        idx = 0 
        while curr.next :
            if idx == p :
                break
            curr = curr.next
            idx += 1
        
        new_node = Node(x)
        if curr.next:
            new_node.next = curr.next
            curr.next.prev = new_node
            curr.next = new_node
            new_node.prev = curr
        else :
            curr.next = new_node
            new_node.prev = curr
            new_node.next = None
        return head
    def delPos(head, x):
        # code here
        if not head :
             return None
        
        if x == 1 :
            head = head.next
            head.prev = None
            return head
        
        idx = 1
        prev,curr = None,head
        while curr :
            if idx == x :
                break
            idx += 1
            prev = curr
            curr = curr.next
        if curr.next :
            prev.next = curr.next
            curr.next.prev = prev
            curr.next  = None
            curr.prev = None
            return head
        else :
            prev.next = None
            curr.prev = None
            return head
        
    