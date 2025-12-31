# not consecutive 1 


def solve(self, idx, n, subset, result):
        if idx == n:
            result.append("".join(subset))
            return
        
        # Option 1: put 0
        subset.append("0")
        self.solve(idx + 1, n, subset, result)
        subset.pop()
        
        # Option 2: put 1 (only if last digit is not 1)
        if len(subset) == 0 or subset[-1] == "0":
            subset.append("1")
            self.solve(idx + 1, n, subset, result)
            subset.pop()

def binstr(self, n):
        result = []
        self.solve(0, n, [], result)
        result.sort()
        return result
