/*
 * @lc app=leetcode.cn id=904 lang=cpp
 *
 * [904] 水果成篮
 * 问题本质是找只包含2种数字的最长子数组
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        if (fruits.empty()) return 0;
        unordered_map<int, int> basket;
        int start = 0;
        int result = 0;
        for (int end=0;end<fruits.size();end++) {
            basket[fruits[end]]++;
            while (basket.size()>2) {
                int left_fruit = fruits[start];
                basket[left_fruit]--;
                if (basket[left_fruit] == 0) {
                    basket.erase(left_fruit);
                }
                start++;
            }
            result = max(result, end-start+1);
        }
        return result;
    }
};
// @lc code=end

