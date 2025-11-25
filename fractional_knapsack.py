import sys

def fractional_knapsack(values: list[float], weights: list[float], capacity: float) -> tuple[float, list[float]]:
    # our goal is to fill the knapsack with the most value possible that fits within the capacity
    # we do this by computing the density, sorting on the density, putting values into tuples
    # we then sort these tuples, and look through each to determine if we can fit the entirety into the knapsack
    # if not, we take a fraction. instantly return once we take a fraction since the knapsack must be full
    
    # to start, create the tuples (density, index, value, weight)
    tuples: list[tuple[float, int, float, float]] = []
    
    for index, value in enumerate(values):
        weight = weights[index]
        density = value / weight
        
        tuples.append((density, index, value, weight))
        
    # now that we have the tuples, we sort by the density
    # we do this because we are literally greedy. it's 3am. you get the idea
    tuples = sorted(tuples, key=lambda tup: tup[0], reverse=True)
    
    
    remaining_capacity = capacity
    total_value = 0
    
    # we need to initialize as 0.0 since we are required to place in original order
    fractions = [0.0] * len(values)
   
    # now, we loop!
    # i intially had the total value as a seperate loop, but after looking back,
    # i realized i could combine them 
    for tup in tuples:
        index = tup[1]
        weight = tup[3]
        value = tup[2] 
        
        if remaining_capacity - weight < 0:
            # we need to take a fraction
            frac = remaining_capacity / weight
            
            total_value += frac * value
            fractions[index] = (frac)
            break
        else: 
            # we take the whole
            remaining_capacity -= weight

            total_value += value
            fractions[index] = 1.0
        
    return (total_value, fractions)

def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0]); W = float(data[1])
    vals = list(map(float, data[2:2+n]))
    wts = list(map(float, data[2+n:2+2*n]))
    total, fracs = fractional_knapsack(vals, wts, W)
    print(total)
    print(" ".join(str(f) for f in fracs))
    
if __name__ == "__main__":
    solve()