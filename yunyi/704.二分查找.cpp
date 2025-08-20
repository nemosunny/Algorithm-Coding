/*
 * @lc app=leetcode.cn id=704 lang=cpp
 *
 * [704] 二分查找
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int arr_len = nums.size();
        int mid_idx = arr_len / 2;
        int left_idx = 0;
        int right_idx = nums.size() - 1;
        if (arr_len == 0) return -1;
        if (nums[left_idx] == target) return left_idx;
        if (nums[right_idx] == target) return right_idx;
        while (left_idx != mid_idx and right_idx != mid_idx) {
            if (nums[mid_idx] == target) return mid_idx;
            else if (nums[mid_idx] < target) {
                left_idx = mid_idx;
                mid_idx = (left_idx + right_idx) / 2; 
            }
            else if (nums[mid_idx] > target) {
                right_idx = mid_idx;
                mid_idx = (left_idx + right_idx) / 2;
            }
        }
        return -1;
    }
};
// @lc code=end

