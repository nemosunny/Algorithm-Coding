# This is the algorithm practice for Leecode 78.
def subsets(nums):
    solutions = []
    path = []
    def back_tracking(start_idx):
        if start_idx == len(nums):
            return
        for i in range(start_idx, len(nums)):
            path.append(nums[i])
            solutions.append(path[:])
            back_tracking(i+1)
            path.pop()
    
    back_tracking(0)
    solutions.append([])
    return solutions
        
            
nums = [1]
results = subsets(nums)
print(f"This is the result: {results}")