n, m = [int(i) for i in input().split()]
matrix = [(list(range(m*i + 1, m*i + 1 + m)) if i % 2 == 0 else(list(range(m*i + 1, m*i + 1 + m)[::-1]))) for i in range(n)]

for row in matrix:
    print(*row)