# This is the algorithm practice for Leecode 47.
def permute_unique(nums):
    solutions = []
    path = []
    nums.sort()
    used = [False] * len(nums) # index级去重，要区分每一个"位置“是否被用过
    def back_tracking():
        if len(path) == len(nums):
            solutions.append(path[:])
            return
        for i in range(0, len(nums)):
            if used[i]: # 控制这个位置是否使用过
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]: # 控制同一层重复值只使用一次
                continue
            used[i] = True
            path.append(nums[i])
            back_tracking()
            path.pop()
            used[i] = False
    back_tracking()
    return solutions
    


nums = [1, 1, 2]
result = permute_unique(nums)
print(f"This is the results: {result}")