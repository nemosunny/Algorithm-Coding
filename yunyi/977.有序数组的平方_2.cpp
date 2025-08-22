/*
 * @lc app=leetcode.cn id=977 lang=cpp
 *
 * [977] 有序数组的平方
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int nums_len = nums.size();
        int neg_idx = -1;
        for (int i=0;i<nums.size();i++) {
            if (nums[i] < 0) neg_idx = i;
            else break;
        }
        vector<int> results;
        int left = neg_idx, right = neg_idx + 1;
        while (left >= 0 || right < nums_len) {
            if (left < 0) {
                results.push_back(nums[right] * nums[right]);
                right++;
            }
            else if (right == nums_len) {
                results.push_back(nums[left] * nums[left]);
                left--;
            }
            else if (nums[left] * nums[left] < nums[right] * nums[right]) {
                results.push_back(nums[left] * nums[left]);
                left--;
            }
            else {
                results.push_back(nums[right] * nums[right]);
                right++;
            }
        }
        return results;
    }
};
// @lc code=end

