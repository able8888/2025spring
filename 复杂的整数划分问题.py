n,k=map(int,input().split())
def f1(n,k):
	dp1=[[0]*(k+1) for _ in range(n+1)]
	dp1[0][0]=1
	for j in range(1,k+1):
		for i in range(1,n+1):#dp[i][j]表示把i分成j个整数
			dp1[i][j]=dp1[i-1][j-1]+dp1[i-j][j]#划分带不带1
	return dp1[n]
def f2(n):
	dp2=[0]*(n+1)
	dp2[0]=1
	for j in range(1,k+1):
		for i in range(1,n+1):

print(int(n//2)+1)
dp3=[[0]*(k+1) for _ in range(n+1)]
dp3[0][0]=1
ans=1
for j in range(1,n+1,2):
	for i in range(j,n+1):
		dp3[i]=dp3[i]+dp3[i-j]
print(dp3[n])
