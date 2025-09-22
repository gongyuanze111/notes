import sys
import numpy as np

H, W, K, _ = map(int, sys.stdin.readline().split())
image = []
strategy = []
for i in range(H):
    image.append(list(map(int, sys.stdin.readline().split())))
for i in range(K):
    strategy.append(list(map(int, sys.stdin.readline().split())))

energy = [[0 for i in range(W)] for j in range(H)]
cir = W // 2
for i in range(H):
    for j in range(W):
        for dk in range(-cir, cir + 1):
            for dl in range(-cir, cir + 1):
                di = i + dk
                dj = j + dl
                if di < 0 or di >= H or dj < 0 or dj >= W:
                    energy[i][j] += 0
                else:
                    energy[i][j] += image[di][dj] * strategy[dk + cir][dl + cir]
dp = [[0 for i in range(W)] for j in range(H)]
for i in range(W):
    dp[0][i] = dp[0][i - 1] + energy[0][i]
for i in range(1, H):
    for j in range(1, W):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1]) + energy[i][j]
max = 0
for i in range(W):
    max = max(max, dp[H - 1][i])
print(max)