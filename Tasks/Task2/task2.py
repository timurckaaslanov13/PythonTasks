s = [[x] for x in input().split()]
for i in range(len(s) - 1, 0, -1):
    if s[i][0] == s[i - 1][0]:
        s[i - 1].extend(s[i])
        del(s[i])
print(s)