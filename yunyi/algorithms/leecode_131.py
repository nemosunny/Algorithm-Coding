# This is the algorithm practice for Leecode 131.

def partition(s):
    # 判断子串是否是回文序列
    def judgement(sub_s):
        len_s = len(sub_s)
        for i in range(0, len_s//2):
            if sub_s[i] != sub_s[len_s-i-1]:
                return False
        return True
    solutions = []
    path = [] # 字串的可能分割
    
    def back_tracking(start_idx):
        if start_idx == len(s):
            solutions.append(path[:])
            return
        for i in range(start_idx, len(s)):
            sub_s = s[start_idx:i+1]
            if judgement(sub_s):
                path.append(sub_s)
                back_tracking(i+1)
                path.pop()
        
    back_tracking(0)
    return solutions

s = "abba"
results = partition(s)
print(f"This is the result: {results}") 