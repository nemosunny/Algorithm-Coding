/*
 * @lc app=leetcode.cn id=209 lang=cpp
 *
 * [209] 长度最小的子数组
 * 该解方使用滑动窗口，本质上是通过滑动窗口的方式使用一个for循环去代替双重循环
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int result = INT_MAX;
        int start=0, end = 0;
        int sum = 0;
        while (end < nums.size()) {
            sum += nums[end];
            while (sum >= target) {
                result = min(result, end-start+1);
                sum -= nums[start];
                start++;
            }
            end++;
        }
        return result == INT_MAX ? 0 : result;
    }
};
// @lc code=end

