# This is algorithm practice for Leecode 455.
def find_content_children(g, s):
    g.sort()
    s.sort()
    satisfied = [0] * len(g)
    i = 0
    j = 0
    while j < len(s) and i < len(g):
        if g[i] <= s[j] and satisfied[i] == 0:
            satisfied[i] = 1
            i += 1
            j += 1
        elif g[i] > s[j]:
            j+= 1
        else:
            print("Unusual Situation!")
    result = sum(satisfied)
    return result
    

g = [1, 2, 3, 4, 5]
s = [1, 1, 2, 3, 4]
result = find_content_children(g, s)
print(f"This is the result: {result}")