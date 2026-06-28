# This is the algorithm solution for Leecode 40.

# 如下算法会超时
# def combination_sum_2(candidates, target):
#     solutions = []
#     path = []
#     def back_tracing(candidates, target, start_idx):
#         if sum(path) == target:
#             solutions.append(sorted(path))
#             return
#         for i in range(start_idx, len(candidates)):
#             if sum(path) + candidates[i] <= target:
#                 path.append(candidates[i])
#                 back_tracing(candidates, target, i+1)
#                 path.pop()
#             else:
#                 pass
#     back_tracing(candidates, target, 0)
#     set_solutions = set(tuple(x) for x in solutions)
#     solutions = list(list(x) for x in set_solutions)
#     return solutions
    
def combination_sum_2(candidates, target):
    candidates.sort()
    solutions = []
    path = []
    def back_tracking(start_idx, remain):
        if remain == 0:
            solutions.append(path[:])
            return
        for i in range(start_idx, len(candidates)):
            # 同一层去重
            if i > start_idx and candidates[i] == candidates[i-1]:
                continue
            # pruning
            if candidates[i] > remain:
                break
            path.append(candidates[i])
            back_tracking(i+1, remain-candidates[i])
            path.pop
    back_tracking(0, target)
    return solutions
            

candidates = [2,5,2,1,2]
target = 5
results = combination_sum_2(candidates, target)
print(f"This is the result: {results}")