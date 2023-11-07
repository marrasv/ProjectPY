def cnk (a,b):
    if a < b:
        return 0
    elif b == 0:
        return 1
    else:
        return (cnk(a - 1, b) + cnk(a - 1, b - 1))
n, k = map(int, input().split())
print(cnk(n,k))