string = input().split()
ls = [[]]
for i in range(len(string) + 1):
    for j in range(i + 1, len(string) + 1):
        f = []
        f.extend(string[i:j])
        ls.append(f)
ls = sorted(ls, key=len)
print(ls)