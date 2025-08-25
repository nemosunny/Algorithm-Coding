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
        int k = 1; // 按照边计数
        int q = k/4; // 按照正方形计数
        int i = 0; // 坐标
        int j = 0;
        int num = 1; // 填入的数值
        vector<vector<int>> results(n, vector<int>(n, 0));
        if (n==1) {
            results[0][0] = 1;
            return results;
        }
        results[i][j] = num;
        num++;
        j++;
        while (num <= 8) {
            if (k%4==1) {
                q = k/4;
                while (j < n-q-1) {
                    results[i][j] = num;
                    j++;
                    num++; 
                }
                k++;
                cout << "Num in 1: " << num << endl;
            }
            else if (k%4==2) {
                q = k/4;
                while (i < n-q-1) {
                    results[i][j] = num;
                    i++;
                    num++;
                }
                k++;
                cout << "Num in 2: " << num << endl;
            }
            else if (k%4==3) {
                q = k/4;
                while (j > q) {
                    results[i][j] = num;
                    j--;
                    num++;
                }
                k++;
                cout << "Num in 3: " << num << endl;
            }
            else {
                q = k/4;
                cout << "q inside: " << q << endl;
                cout << "i inside: " << i << endl;
                cout << "j inside: " << j << endl;
                while (i>=q) {
                    results[i][j] = num;
                    i--;
                    num++;
                    
                }
                k++;
                cout << "Num in 0: " << num << endl;
                // 开启下一轮
                j++;
                results[i][j] = num;
                num++;
            }
        }
        return results;
    }
};
// @lc code=end

