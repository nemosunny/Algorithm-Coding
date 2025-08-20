/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = nums.size();
        int idx = 0;
        int arr_len = nums.size();
        if (nums.size() == 0) return 0;
        while (idx < arr_len) {
            if (nums[idx] == val) {
                k -= 1;
                nums.erase(nums.begin()+idx);
                arr_len -= 1;
            }
            else {
                idx += 1;
            }
        }
        cout << "Num K: " << k;
        return k;
    }
};
// @lc code=end

