# def lengthOfLoop(self, head):
#         #code here
#         my_set = set()
#         curr = head
#         count = 0
#         my_set2 = set()
#         while curr :
#             if curr in my_set :
#                 if curr in my_set2 :
#                     return count
#                 my_set2.add(curr)
#                 count += 1
#             my_set.add(curr)
#             curr = curr.next
#         return count


def lengthOfLoop(self, head):
        #code here
        slow,fast = head,head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                slow = slow.next # due to this c = 1
                count = 1 
                while slow != fast :
                    count += 1
                    slow = slow.next
                return count
        return 0