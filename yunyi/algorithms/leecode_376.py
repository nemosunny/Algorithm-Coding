# This is algorithm practice for Leecode 376.
# def wiggle_max_length(nums):
#     if len(nums) == 1:
#         return 1
#     elif len(nums) == 2 and nums[0] != nums[1]:
#         return 2
#     elif len(nums) == 2 and nums[0] == nums[1]:
#         return 1
#     else:
#         diff_ls = []
#         for i in range(len(nums)-1):
#             if nums[i] < nums[i+1]:
#                 diff_ls.append(1)
#             elif nums[i] > nums[i+1]:
#                 diff_ls.append(-1)
#             else:
#                 diff_ls.append(0)
#         for i in range(len(diff_ls)-1):
#             if diff_ls[i] * diff_ls[i+1] == -1:
#                 i += 1
#             else:

def wiggle_max_length(nums):
    if len(nums) == 1:
        return 1
    elif len(nums) == 2 and nums[0] != nums[1]:
        return 2
    elif len(nums) == 2 and nums[0] == nums[1]:
        return 1
    else:
        diff_ls = []
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                diff_ls.append(1)
            elif nums[i] > nums[i + 1]:
                diff_ls.append(-1)
            else:
                diff_ls.append(0)
        count = 1
        prev = 0
        for d in diff_ls:
            if d == 0:
                continue
            if prev == 0:
                prev = d
                count += 1
            else:
                if d != prev:
                    count += 1
                    prev = d
        return count
    


nums = [1,17,5,10,13,15,10,5,16,8]
result = wiggle_max_length(nums)
print(f"This is the result: {result}")