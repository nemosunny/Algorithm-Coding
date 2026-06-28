# This is the algorithm practice for Leecode 39.

def combination_sum(candidates, target):
    solutions = []
    path = []
    def back_tracing(candidates, target, start_idx):
        if sum(path) == target:
            solutions.append(path[:])
            return
        for i in range(start_idx, len(candidates)):
            if sum(path) + candidates[i] <= target:
                path.append(candidates[i])
                back_tracing(candidates, target, i)
                path.pop()
            else:
                pass
    back_tracing(candidates, target, 0)
    return solutions
    
   
candidates = [2]
target = 1
results = combination_sum(candidates, target)
print(f"This is the result: {results}")
