def setBit(self, n):
		# code here4
		n = n | (n + 1)
		return n