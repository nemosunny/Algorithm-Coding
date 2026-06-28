# This is the algorithm result for Leecode 77.

def solve_back_trace(n, k):
    solutions = []
    path = []
    def back_tracing(n, k, start_idx):
        if len(path) == k:
            solutions.append(path[:])
            return 
        for i in range(start_idx, n+1):
            path.append(i)
            back_tracing(n, k, i+1)
            path.pop()
    back_tracing(n, k, 1)
    return solutions
    
    
n = 4
k = 2
results = solve_back_trace(n, k)
print(f"The results are: {results}")