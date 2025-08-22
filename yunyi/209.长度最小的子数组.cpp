/*
 * @lc app=leetcode.cn id=209 lang=cpp
 *
 * [209] 长度最小的子数组
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int len = 1;
        int start = 0;
        int sum = 0;
        while (len <= nums.size()) {
            start = 0;
            sum = 0;
            while (start <= nums.size()-len) {
                for (int i=start;i<start+len;i++) {
                    sum += nums[i];
                }
                if (sum >= target) return len;
                else {
                    start += 1;
                    sum = 0;
                }
            }
            len += 1;
        }
        return 0;       
    }
};
// @lc code=end

