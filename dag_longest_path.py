import sys
from collections import deque, defaultdict

def dag_longest_path(n: int, edges: list[tuple[int,int,int]]) -> tuple[int, list[int]]:
    # find the longest path from the list of edges for the dag graph
    # we need to topologically sort to start the process, but to do that, we build the graph
    
    graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
    indeg: list[int] = [0] * n

    # we count indeg so we can later use deque to only have nodes with no incoming edges
    for u, v, w in edges:
        graph[u].append((v, w))
        indeg[v] += 1
        
    # now we can topologically sort
    topologically_sorted: list[int] = []
    queue: deque[int] = deque()
    
    # use indeg to build queue
    for i in range(n):
        if indeg[i] == 0:
            queue.append(i)
    
    # use BFS to topologically sort
    while queue:
        u = queue.popleft()
        topologically_sorted.append(u)
        for v, _ in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)

    # we need to initialize the roots of the DAG for DP to infinity
    distance: list[int] = [-10**18] * n
    parent: list[int] = [-1] * n

    # we set the node of the DAG to 0 if they do not have a parent
    # aka root nodes
    for node in topologically_sorted:
        if parent[node] == -1:
            distance[node] = 0

    # use bellman-ford to compute the distances
    for u in topologically_sorted:
        if distance[u] == -10**18:
            continue  
        for v, w in graph[u]:
            if distance[u] + w > distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u

    # grab the highest distance value
    best_end = max(range(n), key=lambda x: distance[x])
    best_value = distance[best_end]

    # backtrace to get the path
    path: list[int] = []
    cur = best_end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return (best_value, path)

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