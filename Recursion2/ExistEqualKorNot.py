def solve(self, idx, total, target, arr):
        if total == target:
            return True
        if idx == len(arr) or total > target:
            return False
        
        # take arr[idx]
        if self.solve(idx + 1, total + arr[idx], target, arr):
            return True
        
        # skip arr[idx]
        if self.solve(idx + 1, total, target, arr):
            return True
        
        return False

def checkSubsequenceSum(self, N, arr, K):
        return self.solve(0, 0, K, arr)