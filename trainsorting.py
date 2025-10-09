#reading number of cars and their inputted weight 
num_cars = int(input())
train_weights = [int(input()) for _ in range(num_cars)]


# for any pivot, 
# cars in front of it is always heavier, and is monotonically increasing
# cars behind it is always lighter, and is monotonically decreasing

max_increasing = [1] * num_cars # Longest Increasing Subsequence
max_decreasing = [1] * num_cars # Longesst Decreasing Subsequence

# for i-th car, store the length of longest increasing subsequence
# e.g., max_increasing[2] = length of LIS of cars that arrive after the 3rd car 

#subproblems transversially filling arrays from last car up to first car 
for current_index in range(num_cars - 1, -1, -1):           # backwards arrival order
    for next_index in range(current_index + 1, num_cars):   # look at cars that arrive after it
        if train_weights[current_index] < train_weights[next_index]: 
            max_increasing[current_index] = max(
                max_increasing[current_index],
                max_increasing[next_index] + 1
            )
        else:
            #can place lighter car in back
            max_decreasing[current_index] = max(
                max_decreasing[current_index],
                max_decreasing[next_index] + 1
            )

#then compute the longest train by considering each car as the pivot
longest_train = 0
for pivot_index in range(num_cars):
    #combine front (increasing) and back (decreasing)
    train_length = max_increasing[pivot_index] + max_decreasing[pivot_index] - 1 # subtract 1 to avoid double counting pivot
    longest_train = max(longest_train, train_length)

print(longest_train)