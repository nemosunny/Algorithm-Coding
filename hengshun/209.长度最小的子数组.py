#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = j = 0
        res = n + 1
        subarr_sum = 0
        while j < n:
            subarr_sum += nums[j]
            j += 1
            while subarr_sum >= target:
                res = min(res, j - i)
                subarr_sum -= nums[i]
                i += 1
        if res == n + 1:
            return 0
        return res

# @lc code=end

