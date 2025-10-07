
def max_movies_watched(e, m):
    e = set(e)
    m = set(m)
    #combine all days has movie E,M like
    liked_all = sorted(e.union(m))
    n = len(liked_all)
    
    dislikes = []
    for day in liked_all:
        if day in e and day in m:
            dislikes.append(0)
        elif day in e:
            dislikes.append(2)
        else:
            dislikes.append(1)

    #bottom up-> create 2d list
    #n+1 rows and 3 columns (3 possible dislike state)
    dp = [[0] * 3 for _ in range(n + 1)]

    #iterate from the last movie day back to the first
    for i in range(n - 1, -1, -1):
        for prev_dislike in range(3): #loop through 3 possible dislike state
            #skip option
            skip = dp[i + 1][prev_dislike]

            #watch movie if allowed.
            watch = 0
            curr = dislikes[i]
            if curr == 0 or curr != prev_dislike:
                watch = 1 + dp[i + 1][curr]

            dp[i][prev_dislike] = max(skip, watch)

    return dp[0][0]

E = list(map(int, input().split()))
liked_E = E[1:]
M = list(map(int, input().split()))
liked_M = M[1:]

print(max_movies_watched(liked_E, liked_M))
