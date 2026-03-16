#User function template for Python

class Solution:
	def floydWarshall(self, dist):
		#Code here
		n = len(dist)
		for via in range(n):
		    for i in range(n):
		        for j in range(n):
		            if dist[i][via] != 10** 8 and dist[via][j] != 10**8:
		                dist[i][j] = min(dist[i][j] , dist[i][via] + dist[via][j])
		return dist

# in this question it might contain -ve weight so we will use this
# but if no -ve cost then we can also use dijkrsta for all nodes -> (ElogV) * V