n = int(input().strip())
W = []
for _ in range(n):
    W.append(int(input().strip()))

LIS = [1] * len(W)
LDS = [1] * len(W)

for i in range(len(W) - 1, -1, -1):
    for j in range(i + 1, len(W)):
        if W[i] < W[j]:
            LIS[i] = max(LIS[i], 1 + LIS[j])
        else:
            LDS[i] = max(LDS[i], 1 + LDS[j])

best = 0
for pivot in range(n):
    order = LIS[pivot] + LDS[pivot] - 1
    best = max(best, order)

print(best)
