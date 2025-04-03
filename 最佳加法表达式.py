def min_addition_expression(s, m):
	n = len(s)
	dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
	if n<m+1:
		dp[n][m]=float('inf')


	for i in range(1, n + 1):
		dp[i][0] = int(s[:i])

	for j in range(1, m + 1):
		for i in range(1, n + 1):
			for k in range(1, i):
				dp[i][j] = min(dp[i][j], dp[k][j - 1] + int(s[k:i]))

	return dp[n][m]

while True:
	try:
		m=int(input())
		s=input()
		print(min_addition_expression(s, m))
	except EOFError:
		break
