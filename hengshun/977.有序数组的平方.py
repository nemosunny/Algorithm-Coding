#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n - 1
        res = [0 for _ in range(n)]
        k = n - 1
        while i <= j and k >= 0:
            if nums[i] ** 2 <= nums[j] ** 2:
                res[k] = nums[j] ** 2
                j -= 1
            elif nums[i] ** 2 > nums[j] ** 2:
                res[k] = nums[i] ** 2
                i += 1
            k -= 1
        return res
# @lc code=end

