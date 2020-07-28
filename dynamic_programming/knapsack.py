V_SUM_MAX = 1000
N_MAX = 100
W_MAX = 10000000

dp = [[0 for i in range(N_MAX)] for i in range(V_SUM_MAX+1)]
v = [[0 for i in range(N_MAX)] for i in range(V_SUM_MAX+1)]

print(dp)
print(v)


def solve_dp(r, i, w, val, n):
    pass


def max_weight(w,val,n,C):
    # Base cases
    # for i in range(V_SUM_MAX, -1, -1):
        # if solve_dp(i, 0, w, val, n) <= C):
        #     return i

    return 0


if __name__ == '__main__':
    w = [3,4,5]
    val=[30,50,60]
    n=len(w)
    C=8

    print(max_weight(w,val,n,C))