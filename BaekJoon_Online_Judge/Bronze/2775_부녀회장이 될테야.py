tests = int(input())

for test in range(tests):
    k = int(input())
    n = int(input())

    apt = [[_ for _ in range(1, n+1)] for _ in range(k+1)]

    for i in range(1, k+1):
        for j in range(n):
            if j == 0:
                apt[i][j] = 1
            else:
                apt[i][j] = apt[i][j-1] + apt[i-1][j]

    print(apt[k][n-1])