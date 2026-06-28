# This is the solution for leecode 216 with pruning.

def solve(n, k):
    solutions = []
    path = []
    def back_tracing(n, k, start_idx):
        if len(path) == k:
            if sum(path) == n:
                solutions.append(path[:])
            return
        for i in range(start_idx, 10-(k-len(path))+1):
            path.append(i)
            back_tracing(n, k, i+1)
            path.pop()
            
    back_tracing(n, k, 1)
    return solutions
    
    
n = 7
k = 3
results = solve(n, k)
print(f"The results are: {results}")