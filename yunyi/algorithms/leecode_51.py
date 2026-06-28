# This is the algorithm for Leecode 51: N Queens

def solveNQueens(n):
    solutions = []
    board = [["." for _ in range(n)] for _ in range(n)]
    cols = set()
    pos_diag = set() # row+col
    neg_diag = set() # row-col
    
    def backtrack(row):
        # 递归终止条件
        if row == n:
            sol_copy = ["".join(r) for r in board]
            solutions.append(sol_copy)
            return solutions
        # 依次处理该行的每一个列
        for col in range(n):
            # 检查该位置是否能放置Q
            if col in cols or row+col in pos_diag or row-col in neg_diag:
                continue
            # 放置Q
            board[row][col] = 'Q'
            cols.add(col)
            pos_diag.add(row+col)
            neg_diag.add(row-col)
            # 递归
            backtrack(row+1)
            # 没有从终止条件出去，而是到了这里，说明这个方案并不可行，回溯一步
            board[row][col] = '.'
            cols.remove(col)
            pos_diag.remove(row+col)
            neg_diag.remove(row-col)
    backtrack(0)
    return solutions
        

results = solveNQueens(4)
for i, sol in enumerate(results):
    print(f"Solution {i+1}: ")
    for row in sol:
        print(row)
    print("-" * 10)
