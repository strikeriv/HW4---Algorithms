import sys

def fractional_knapsack(values: list[float], weights: list[float], capacity: float) -> tuple[float, list[float]]:
    return (0, [0])

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