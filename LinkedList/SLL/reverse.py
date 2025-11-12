def reverseList(head) :
        prev,temp,front = None,head,head
        while temp :
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
        