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
        int i = 0;
        int j = nums.size()-1;
        int nums_len = nums.size();
        int k = 0;
        int temp = 0;
        vector<int> results(nums_len);
        if (nums_len == 1) {
            results[0] = nums[0] * nums[0];
            return results;
        }
        while (i<j) {
            if (abs(nums[i]) >= abs(nums[j])) {
                temp = nums[i] * nums[i];
                results[nums_len-k-1] = temp;
                k++;
                i++;
            }
            else {
                temp = nums[j] * nums[j];
                results[nums_len-k-1] = temp;
                k++;
                j--;
            }
        }
        if (k != nums.size()) results[0] = nums[i] * nums[i];
        for (int i=0;i<results.size();i++) {
            cout << results[i] << " ";
        }
        return results;
    }
};
// @lc code=end

