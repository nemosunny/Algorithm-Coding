# This is the algorithm practice for Leecode 491.
# 下列解答有问题，会导致只要一个数字在前面出现过就跳过
# def find_subsequences(nums):
#     solutions = []
#     path = []
#     def is_duplicate(num, nums, idx):
#         for i in range(0, idx):
#             if nums[i] == num:
#                 return True
#         return False
    
#     def back_tracking(start_idx):
#         last_element = nums[0]
#         if start_idx == len(nums):
#             return
#         for i in range(start_idx, len(nums)):
#             # pruning
#             if i > start_idx and is_duplicate(nums[i], nums, i):
#                 continue
#             if len(path) == 0:
#                 path.append(nums[i])
#                 back_tracking(i+1)
#                 path.pop()
#             elif nums[i] >= path[-1]:
#                 path.append(nums[i])
#                 if len(path) > 1:
#                     solutions.append(path[:])
#                 back_tracking(i+1)
#                 path.pop()
#     back_tracking(0)
#     return solutions

def find_subsequences(nums):
    solutions = []
    path = []
    def back_tracking(start_idx):
        if len(path) >=2:
            solutions.append(path[:])
        if start_idx == len(nums):
            return
        used = set()
        for i in range(start_idx, len(nums)):
            if nums[i] in used:
                continue
            if len(path) > 0 and nums[i] < path[-1]:
                continue
            path.append(nums[i])
            back_tracking(i+1)
            path.pop()
    back_tracking(0)
    return solutions
    
    
nums = [4, 7, 6]
results = find_subsequences(nums)
print(f"This is the result: {results}")