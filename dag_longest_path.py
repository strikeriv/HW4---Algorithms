import sys
from collections import deque, defaultdict

def dag_longest_path(n: int, edges: list[tuple[int,int,int]]) -> tuple[int, list[int]]:
    return (0, [0])

def solve():
    it = iter(sys.stdin.read().strip().split())
    n = int(next(it)); m = int(next(it))
    edges: list[tuple[int, int, int]] = []
    
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u, v, w))
        
    best, path = dag_longest_path(n, edges)
    print(best)
    print(" ".join(map(str, path)))
    
if __name__ == "__main__":
    solve()