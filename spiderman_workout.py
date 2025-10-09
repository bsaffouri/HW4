def solution(m):
    max_h = sum(m)
    n = len(m)

    dp = [[(float("inf"), "")] * (max_h + 1) for _ in range(n + 1)]
    dp[0][0] = (0, "")

    for i in range(1, n + 1):
        movement = m[i - 1]
        for h in range(max_h + 1):
            above_path = ""
            above = h + movement
            peak_height_above = float("inf")
            if above <= max_h:
                peak_height_above = dp[i - 1][above][0]
                above_path = dp[i - 1][above][1] + "D"

            below_path = ""
            below = h - movement
            peak_height_below = float("inf")
            if below >= 0:
                peak_height_below = max(dp[i - 1][below][0], h)
                below_path = dp[i - 1][below][1] + "U"

            if peak_height_above < peak_height_below:
                dp[i][h] = (peak_height_above, above_path)
            else:
                dp[i][h] = (peak_height_below, below_path)

    print("IMPOSSIBLE") if dp[n][0][0] == float("inf") else print(dp[n][0][1])


num_inputs = int(input())
for _ in range(num_inputs):
    input()
    m = list(map(int, input().split()))

    solution(m)
