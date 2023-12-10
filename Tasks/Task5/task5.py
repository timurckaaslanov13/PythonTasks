n, m = int(input()), int(input())
matric = [[int(x) for x in input().split()]for _ in range(n)]
i, j = map(int, input().split())
for k in range(n):
    matric[k][i], matric[k][j] = matric[k][j], matric[k][i]
    print(*matric[k])