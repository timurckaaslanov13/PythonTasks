def chunked(spis, num):
    ls = [spis[i:i+num]for i in range(0, len(spis), num)]
    return ls
s = input().split()
n = int(input())
print(chunked(s, n))