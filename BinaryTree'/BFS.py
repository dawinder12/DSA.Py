# Level Order Search

from collections import deque
from typing import Optional, List

class Solution:
    def ans(self, node, order):
        queue = deque([])
        queue.append(node)

        while len(queue) > 0:
            level = []                 # FIX 1: level list
            size = len(queue)          # FIX 2: capture level size

            for _ in range(size):      # FIX 3: process one level
                e = queue.popleft()
                if e:
                    level.append(e.val)

                if e and e.left:
                    queue.append(e.left)
                if e and e.right:
                    queue.append(e.right)

            order.append(level)        # FIX 4: append level, not value

        return order

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:                   # FIX 5: null root guard
            return []
        return self.ans(root, [])
