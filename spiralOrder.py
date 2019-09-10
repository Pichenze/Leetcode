class Solution:
	def spiralOrder(self, matrix):
		if matrix == []:
			return []
		m,n = len(matrix),len(matrix[0])
		# visited = m*[n*[False]] #这样生成的列表，修改其中一个，相同列的也会改变，所以不能用，要用列表生成式
		visited = [[False for j in range(n)] for i in range(m)] #访问矩阵，用列表生成式生成，不会出现上面的情况
		result = []
		dire = 0
		i,j = 0,0
		result.append(matrix[i][j])
		visited[i][j] = True
		vt = 1
		while vt < m*n:
			if dire%4 == 0: # 往右
				while j+1 <= n-1 and visited[i][j+1] == False:
					j += 1
					result.append(matrix[i][j])
					visited[i][j] = True
					vt += 1
				dire += 1
			elif dire%4 == 1: # 往下
				while i+1 <= m-1 and visited[i+1][j] == False:
					i += 1
					result.append(matrix[i][j])
					visited[i][j] = True
					vt += 1
				dire += 1
			elif dire%4 == 2: #往左
				while j-1 >= 0 and visited[i][j-1] == False:
					j -= 1
					result.append(matrix[i][j])
					visited[i][j] = True
					vt += 1
				dire += 1
			elif dire%4 == 3: #往上
				while i-1 >= 0 and visited[i-1][j] == False:
					i -= 1
					result.append(matrix[i][j])
					visited[i][j] = True
					vt += 1
				dire += 1
		return result
