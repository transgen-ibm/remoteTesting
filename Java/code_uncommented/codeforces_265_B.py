
# <START-OF-CODE>
n = int(input())
arr = list(map(int, input().split()))
ans = arr[0] + 1
for i in range(1, n):
    ans += abs(arr[i] - arr[i-1]) + 2
print(ans)
# 