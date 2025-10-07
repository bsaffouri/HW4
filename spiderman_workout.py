from collections import defaultdict


def find_best(sequence):
    possible = defaultdict(tuple)  # {height : ("path", peak_height)}
    possible[0] = ("", 0)  # {0 : ("", 0)}

    for num in sequence:
        newdict = {}
        for height, (path, peak_height) in possible.items():

            # up
            up = height + num
            new_up_path = path + "U"
            new_up_height = peak_height if peak_height > up else up
            # check if duplicates exist
            if up not in newdict.keys():
                newdict[up] = (new_up_path, new_up_height)
            else:
                # replace only if new path has lower peak height
                if newdict[up][1] > new_up_height:
                    newdict[up] = (new_up_path, new_up_height)

            # down
            down = height - num
            if down >= 0:
                new_down_path = path + "D"
                new_down_height = peak_height if peak_height > down else down
                # skip if it goes below 0
                if down is None:
                    continue

                # check if duplicates exist
                if down not in newdict.keys():
                    newdict[down] = (new_down_path, new_down_height)
                else:
                    # replace only if new path has lower peak height
                    if newdict[down][1] > new_down_height:
                        newdict[down] = (new_down_path, new_down_height)
        possible = newdict

    print(possible[0][0] if 0 in possible.keys() else "IMPOSSIBLE")


num_input = int(input())
for _ in range(num_input):
    _ = input()
    sequence = list(map(int, input().strip().split()))
    find_best(sequence)
