import sys

n = int(sys.stdin.readline().strip())
l1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
queries = list(map(int, sys.stdin.readline().split()))

dp_max = sum(l1)
dp = [False] * (dp_max + 1)
dp[0] = True

for weight in l1:
    new_dp = dp[:]
    for j in range(dp_max, -1, -1):
        if dp[j]:
            if j + weight <= dp_max:
                new_dp[j + weight] = True
            new_dp[abs(j - weight)] = True
    dp = new_dp

for q in queries:
    print("Y" if q <= dp_max and dp[q] else "N", end=" ")
