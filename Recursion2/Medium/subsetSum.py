def solve(self,idx,arr,sum,result):
        if idx == len(arr):
            result.append(sum)
            return
        sum += arr[idx]
        self.solve(idx + 1 , arr,sum,result)
        sum -= arr[idx]
        self.solve(idx + 1 ,arr,sum,result)
def subsetSums(self, arr):
		# code here
		sum = 0
		result = []
		self.solve(0,arr,sum,result)
		return result