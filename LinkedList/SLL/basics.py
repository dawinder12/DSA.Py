class Node :
    def __init__(self,val):
        self.val = val
        self.next = None

class SinglyLinkedList :
    def __init__(self):
        self.head = None
    
    
    def append(self,val): # O(n)
        if self.head is None :
            self.head = Node(val)
        else :
            curr = self.head
            while curr.next is not None :
                curr = curr.next 
            curr.next = Node(val)
            
    def traverse(self): # O(n)
        if self.head is None :
            print("LL is Empty")
        
        else :
            curr = self.head
            while curr is  not None :
                if curr.next is None :
                    print(curr.val)
                    curr = curr.next
                else : 
                    print(curr.val , end = "->")
                    curr = curr.next
                    
    def insert(self,idx,val):
        if idx == 0 :
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        else :
            new_node = Node(val)
            new_node.next = None
            count = 0
            prev = None
            curr = self.head
            while curr is not None and count <  idx :
                prev = curr
                curr = curr.next
                count += 1
            new_node.next = curr
            prev.next = new_node
    def delete(self,val):
        if self.head.val == val :
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
        else :
            prev = None
            curr = self.head
            found = False
            while curr is not None :
                prev = curr
                curr = curr.next
                if curr.val == val :
                    found  = True
                    prev.next = curr.next
                    temp = curr
                    temp.next = None
                    del temp
                    return
            if not found :
                print("This val is not present in LL ")
                
sll = SinglyLinkedList()
sll.traverse()

sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)

sll.traverse()
sll.insert(3,69)

sll.traverse()


sll.delete(1)
sll.traverse()
sll.delete(4)
sll.traverse()
    
    
        
        

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# # But this method is not efficient so we will create a  class of SLL 

# print(node1.next)
# print(node2)