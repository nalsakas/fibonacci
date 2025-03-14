def dfs(i, j, n):
    if n == 0:
       return j
    
    # replace i and j with new values and decrease number n.
    ret = dfs(j, i + j, n - 1)
    return ret

def bfs(i, j, n):
    for _ in range(n):
        old_i = i 
        i = j
        j = old_i + j
    return j

def fib_dfs(n):
    if n == 1: return 0
    if n == 2: return 1

    # Since n == 1 and n == 2 already generated (pre-determined)
    # Generate nth Fib number, by execute dfs 2 ierations less.
    res = dfs(0, 1, n - 2)
    return res

def fib_bfs(n):
    if n == 1: return 0
    if n == 2: return 1

    # Since n == 1 and n == 2 already generated (pre-determined)
    # Generate nth Fib number, by execute bfs 2 ierations less.
    res = bfs(0, 1, n - 2)
    return res


print(fib_dfs(1), fib_dfs(2), fib_dfs(3), fib_dfs(4), fib_dfs(5), fib_dfs(6), sep=" ")
print(fib_bfs(1), fib_bfs(2), fib_bfs(3), fib_bfs(4), fib_bfs(5), fib_bfs(6), sep=" ")
print(fib_dfs(50))