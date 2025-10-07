#reading number of cars and their inputted weight 
num_cars = int(input())
train_weights = [int(input()) for _ in range(num_cars)]

#base case set to 1
max_increasing = [1] * num_cars #bigger cars are added to the front of the train
max_decreasing = [1] * num_cars #smaller cars are added to the back of the train 

#subproblems transversially filling arrays from last car up to first car 
for current_index in range(num_cars - 1, -1, -1):
    for next_index in range(current_index + 1, num_cars):
        if train_weights[current_index] < train_weights[next_index]:
            #can place heavier car in front
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
    train_length = max_increasing[pivot_index] + max_decreasing[pivot_index] - 1
    longest_train = max(longest_train, train_length)

print(longest_train)