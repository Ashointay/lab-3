def all_permutations(s):
    if len(s) == 1:
        return [s] 
    per = []
    for i in range(len(s)):
        char = s[i]
        r = s[:i]+s[i+1:]
        for p in all_permutations(r):
            per.append(char + p)
    return per 
s = input()
print(all_permutations(s))