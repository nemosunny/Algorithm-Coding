/*
 * @lc app=leetcode.cn id=59 lang=cpp
 *
 * [59] 螺旋矩阵 II
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int max_num = n*n;
        int cur_num = 1;
        int row=0, column=0;
        vector<vector<int>> results(n, vector<int>(n));
        vector<vector<int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int direct_idx = 0;
        while (cur_num <= max_num) {
            results[row][column] = cur_num;
            cur_num++;
            int next_row = row + directions[direct_idx][0];
            int next_col = column + directions[direct_idx][1];
            if (next_row >= n || next_row < 0 || next_col >= n || next_col < 0 || results[next_row][next_col]!=0) {
                direct_idx = (direct_idx+1) % 4;
            }
            row = row + directions[direct_idx][0];
            column = column + directions[direct_idx][1];
        }
        return results;
    }
};
// @lc code=end

