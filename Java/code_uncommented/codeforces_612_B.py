
# <START-OF-CODE>

n = int(input())
dp = [0] * 200001
for i in range(n):
    dp[int(input())] = i
ans = 0
for i in range(2, n):
    ans += abs(dp[i] - dp[i-1])
print(ans)

# 