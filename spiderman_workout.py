from collections import defaultdict

# idea: for all possible reachable height at each move, keep the best path and update it
# bottom-up


def find_best(sequence):
    possible = {0: ("", 0)}  # initialization, {height : ("path", peak_height)}

    for num in sequence:
        newdict = {}  # dictionary at each state

        # build on top of possible states; key = height, value = (path, peak_height)
        for height, (path, peak_height) in possible.items():
            # up
            up = height + num                    # height when you decide to go up
            new_up_path = path + "U"             # path when you decide to go up
            # update peak height for the path
            new_up_height = max(peak_height, up)

            # check for duplicate keys; if it doesn't exist, it has never been reached.
            if up not in newdict:
                newdict[up] = (new_up_path, new_up_height)
            else:  # if there are multiple ways to reach the same height, choose path with lower peak height
                if newdict[up][1] > new_up_height:
                    newdict[up] = (new_up_path, new_up_height)

            # down
            down = height - num
            if down >= 0:  # consider only when path stays above ground
                new_down_path = path + "D"
                new_down_height = max(down, peak_height)
                # check if duplicates exist
                if down not in newdict:
                    newdict[down] = (new_down_path, new_down_height)
                else:
                    # replace only if new path has lower peak height
                    if newdict[down][1] > new_down_height:
                        newdict[down] = (new_down_path, new_down_height)
        possible = newdict
        # print(newdict)

    if 0 in possible:  # ground level is reachable
        print(possible[0][0])
    else:
        print("IMPOSSIBLE")


num_input = int(input())
for _ in range(num_input):
    _ = input()
    sequence = list(map(int, input().strip().split()))
    find_best(sequence)
