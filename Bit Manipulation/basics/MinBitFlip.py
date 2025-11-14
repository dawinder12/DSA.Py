def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start and goal :
            if start & 1 != goal & 1 :
                count += 1
            start = start >> 1
            goal = goal >> 1
        while start :
            if start & 1 == 1 :
                count += 1
            start = start >> 1
        while goal :
            if goal & 1 == 1 :
                count += 1
            goal = goal >> 1
        return count