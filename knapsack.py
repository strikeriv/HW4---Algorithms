import array
import sys

def knapsack(values: list[int], weights: list[int], capacity: int) -> tuple[int, list[int]]:
    
    # for DP, we construct a 2d array to hold the values we have already computed
    # the rows signify the items, and the columns are the max values that we have computed
    # construct the array with 0's initially with the size we set above
    num_values = len(values) + 1
    num_max_values = capacity + 1
    
    table: list[list[int]] = [[0] * num_values for _ in range(num_max_values)]
    
    # outer loop handles each item (each row in the table)
    for i in range(1, num_values):
        
        weight = weights[i]
        value = values[i]
        
        # inner loop handles each permutation of capacity in the table
        for w in range(num_max_values):
            # grab the previous max value by i - 1 (since zero based), and previouly calculated max value
            # this value is current as long as next condition holds
            previous_weight = table[i - 1][w]
            
            # we check to see if the weight is greater than previous
            if weight <= w:
                
            else:  
                new = table[i - 1][w] + values[i]
            
            
        
    return (0, [0])
    
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