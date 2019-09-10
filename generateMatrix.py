class Solution:
	def generateMatrix(self, n: int) -> List[List[int]]:
		matrix = [[0 for j in range(n)] for i in range(n)]
		dire = 0
		i,j = 0,0
		matrix[i][j] = 1
		vt = 1
		while vt < n*n:
			if dire%4 == 0: # 往右
				while j+1 <= n-1 and matrix[i][j+1] == 0:
					vt += 1
					j += 1
					matrix[i][j] = vt
				dire += 1
			elif dire%4 == 1: # 往下
				while i+1 <= n-1 and matrix[i+1][j] == 0:
					vt += 1
					i += 1
					matrix[i][j] = vt
				dire += 1
			elif dire%4 == 2: #往左
				while j-1 >= 0 and matrix[i][j-1] == False:
					vt += 1
					j -= 1
					matrix[i][j] = vt					
				dire += 1
			elif dire%4 == 3: #往上
				while i-1 >= 0 and matrix[i-1][j] == False:
					vt += 1
					i -= 1
					matrix[i][j] = vt
				dire += 1
		return matrix
