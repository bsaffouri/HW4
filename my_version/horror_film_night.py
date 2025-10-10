E = list(map(int, input().split()))
M = list(map(int, input().split()))

E = set(E[1:])
M = set(M[1:])

all = sorted(list(E | M))
dislikes = []

for movie in all:
    if movie in E and movie in M:
        dislikes.append(0)  # both likes
    elif movie in E:
        dislikes.append(1)  # Marcos dislikes
    elif movie in M:
        dislikes.append(2)  # Emma dislikes

dp = [[0] * 3 for _ in range(len(all) + 1)]
states = [0, 1, 2]  # 0: both like, 1: Marcos dislikes, 2: Emma dislikes

for movie in range(len(all) - 1, -1, -1):
    current_disliker = dislikes[movie]
    for state in range(3):
        previous_disliker = states[state]
        skip = dp[movie + 1][state]
        watch = dp[movie + 1][current_disliker] + 1

        if previous_disliker == current_disliker and current_disliker != 0:
            dp[movie][state] = skip
        else:
            dp[movie][state] = max(skip, watch)


print(dp[0][0])
