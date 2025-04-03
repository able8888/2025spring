N,K=map(int,input().split())
n=K-N
if n==0:
    print(0)
elif n<0:
    print(n-1)
else:
    dp=[float('-inf')]*N+[0]*n
    for i in range(n):
        if i%2!=0:
            dp[i]=min(dp[i-1]+1,dp[i+1]+1,dp   )

