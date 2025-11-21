import sys

def knapsack(values: list[int], weights: list[int], capacity: int) -> tuple[int, list[int]]:
    
    # for DP, we construct a 2d array to hold the values we have already computed
    # the rows signify the items, and the columns are the max values that we have computed
    # construct the array with 0's initially with the size we set above
    # TLDR; table holds maximum value
    num_values = len(values) + 1
    num_max_values = capacity + 1
    
    table: list[list[int]] = [[0] * num_max_values for _ in range(num_values)]
    
    # outer loop handles each item (each row in the table)
    for i in range(1, num_values):
        
        # grab values (zero based so we sub 1)
        weight = weights[i - 1]
        value = values[i - 1]
        
        # inner loop handlaes each permutation of capacity in the table
        for w in range(num_max_values):
            # grab the previous max value by i - 1 (since zero based)
            previous_weight = table[i - 1][w]
            
            # check if the current capacity weight is less than the
            # weight of the valye we are iterating through
            if weight <= w:
                # since current loop weight is less than value weight, we are adding
                # grab the max we can do when included
                previous_max = table[i - 1][w - weight]
                new_max = previous_max + value
                
                # assign best, as it fills up most capacity
                table[i][w] = max(previous_weight, new_max)
            else:  
                # capacity is exceeded, so we must use the previous weight
                table[i][w] = previous_weight
            
  
    # max value is located in far right of matrix
    max_capacity = table[num_values - 1][num_max_values - 1]

    # we perform back tracing to find the values
    capacity_values: list[int] = []
    curr_weight = capacity
    
    for i in range(num_values - 1, 0, -1):
        curr_capacity = table[i][curr_weight]
        prev_capacity = table[i - 1][curr_weight]
        
        # check if they are equal
        # if not, means the value is included in the knapsack
        # add to capacity values, and reduce weight by values weight
        if curr_capacity != prev_capacity:
            capacity_values.append(i-1)
            curr_weight -= weights[i-1]
    
    capacity_values.reverse()
    
    return (max_capacity, capacity_values)
    
def solve():
    data = sys.stdin.read().strip().split()
    n, W = map(int, data[:2])
    vals = list(map(int, data[2:2+n]))
    wts = list(map(int, data[2+n:2+2*n]))
    best, idxs = knapsack(vals, wts, W)
    print(best)
    print(" ".join(map(str, idxs)))
    
if __name__ == "__main__":
    solve()