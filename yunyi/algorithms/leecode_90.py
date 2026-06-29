# This is the algorithm practice for Leecode 90.
def subsets_with_dup(nums):
    nums.sort()
    solutions = []
    path = []
    def back_tracking(start_idx):
        if start_idx == len(nums):
            return
        for i in range(start_idx, len(nums)):
            if i > start_idx and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            solutions.append(path[:])
            back_tracking(i+1)
            path.pop()
    back_tracking(0)
    solutions.append([])
    return solutions
    
    
nums = [4, 4, 4, 1, 4]
results = subsets_with_dup(nums)
print(f"This is the result: {results}")