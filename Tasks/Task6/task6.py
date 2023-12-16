n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
for x in matrix[::-1]:
    print(*x)