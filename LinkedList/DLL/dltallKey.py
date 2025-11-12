def deleteAllOccurOfX(self, head, x):
    # delete all occurrences of x from doubly linked list
        curr = head
        new_head = head

        while curr:
            if curr.data == x:
            # update links to remove curr
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
            # update head if first node deleted
                if curr == new_head:
                    new_head = curr.next
            # move forward after deletion
                curr = curr.next
            else:
            # move normally if not deleted
                prev = curr
                curr = curr.next

        return new_head
