def removeNthFromEnd(head, n) :
        if not head or not head.next :
            return None
        n1,n2 = head,head
        while n :
            n2 = n2.next 
            n -= 1
        if not n2 :
            return head.next
        while n2.next :
            n1 = n1.next
            n2 = n2.next
        n1.next = n1.next.next
        return head