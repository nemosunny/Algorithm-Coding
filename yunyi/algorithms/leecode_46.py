# This is the algorithm practice for Leecode 46.
# 下列算法是组合的思路并不是排列的思路
# def permute(nums):
#     solutions = []
#     path = []
#     def back_tracking(current_idx):
#         if len(path) == len(nums):
#             solutions.append(path[:])
#             return
#         for i in range(0, len(nums)):
#             if nums[i] not in path:
#                 path.append(nums[i])
#                 back_tracking(i+1)
#                 path.pop()
#     back_tracking(0)
#     return solutions    


def permute(nums):
    solutions = []
    path = []
    used = set()
    def back_tracking():
        if len(path) == len(nums):
            solutions.append(path[:])
            return
        for i in range(0, len(nums)):
            if nums[i] in used:
                continue
            used.add(nums[i])
            path.append(nums[i])
            back_tracking()
            path.pop()
            used.remove(nums[i]) # 同步需要pop出去
    back_tracking() # 可以直接不传参数
    return solutions


nums = [1, 2, 3]
results = permute(nums)
print(f"This is the result: {results}")