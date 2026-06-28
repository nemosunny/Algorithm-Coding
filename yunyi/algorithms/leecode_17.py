# This is the alogrithm solution for Leecode 17.

def letter_combinations(s):
    num_digits = len(s) # the number of digits
    letter_map = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                  "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "s"],
                  "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
    solutions = []
    path = []
    def back_tracing(num_digits, current_idx):
        if len(path) == num_digits:
            sol_copy = "".join(path)
            solutions.append(sol_copy)
            return solutions
        current_len = len(letter_map[s[current_idx]])
        for i in range(current_len):
            path.append(letter_map[s[current_idx]][i])
            back_tracing(num_digits, current_idx+1)
            path.pop()
    back_tracing(num_digits, 0)
    return solutions
            
            
s = "234"
results = letter_combinations(s)
print(f"The results are: {results}")