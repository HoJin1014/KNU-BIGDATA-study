def mysum(n, m):
    return(m * (m - 1) - n * (n - 1)) // 2

n, m = map(int, input().split())
print(mysum(n, m))

print(sum(range(n, m + 1)))

