def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        if not head :
            return []
        tail = head
        while tail.next :
            tail = tail.next
        ans = []
        curr = head
        while curr and tail and curr.data <= tail.data :
            a = curr.data
            b = tail.data
            if a + b == target and a != b:
                ans.append([a,b])
                curr = curr.next
                tail = tail.prev
            elif a + b > target :
                tail = tail.prev
            else :
                curr = curr.next
        return ans
                