def reverse(head):
        # code here
        if not head.next or not head:
            return head
        prev,curr = None,head
        while curr :
            front = curr.next
            curr.next = prev
            curr.prev = front
            prev = curr
            curr = front
        return prev