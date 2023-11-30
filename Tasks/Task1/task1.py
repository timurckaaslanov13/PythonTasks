def pascal(n):
    ls = [[1], [1, 1]]
    if n > 1:
        for _ in range(n):
            new_l = [1, 1]
            l = ls[-1]
            for i in range(len(l) - 1):
                new_l.insert(new_l[i + 1], l[i] + l[i + 1])
            ls.append(new_l)

    return ls[n]


n = int(input())
print(pascal(n))