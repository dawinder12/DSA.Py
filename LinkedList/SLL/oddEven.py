def oddEvenList(head): 
        if not head or not head.next :
            return head
        even_head = head.next
        odd = head
        even = head.next
        while even and even.next :
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return head
    
# ek hi loop mai odd and even ki alg list bana do fir unko join kardo