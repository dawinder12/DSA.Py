def removeDuplicates(self, head):
        # code here
        # return head after editing list
        if not head :
            return None
        prev = head
        curr = head.next
        while curr:
            if curr.data == prev.data :
                prev.next = curr.next
                if curr.next :
                    curr.next.prev = prev
                else :
                    curr.prev = prev
                curr = curr.next
            else :
                prev = curr
                curr = curr.next
        return head