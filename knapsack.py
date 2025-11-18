import sys

def knapsack(values: list[int], weights: list[int], capacity: int) -> tuple[int, list[int]]:
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