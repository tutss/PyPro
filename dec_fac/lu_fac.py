import numpy as np
import scipy as sp

def pivot_matrix(A):
    n = len(A)
    id = np.identity(n)

    for j in range(n):
        row = max(range(j, n), key=lambda i: abs(A[i][j]))
        if (j != row):
            id[j], id[row] = id[row], id[j]

    return id

def lu(A):
    n = len(A)
    l = [[0.0] * n for i in range(n)]
    u = [[0.0] * n for i in range(n)]
    p = pivot_matrix(A)
    pa = np.matmul(p, A)

    for j in range(len(A)):

        # Getting U
        for i in range(j+1):
            s = sum(u[k][j] * l[k][i] for k in range(i))
            u[i][j] = pa[i][j] - s

        # Getting L
        for i in range(j+1):
            s = sum(u[k][j] * l[k][i] for k in range(i))
            l[i][j] = (pa[i][j] - s) / u[j][j]

    return (p, l, u)


def main():
    A = np.array([[7, 3, -1, 2],
                  [3, 8, 1, -4],
                  [-1, 1, 4, -1],
                  [2, -9, -1, 6]])
    P, L, U = lu(A)
    # p_1, l_1, u_1 = sp.linalg.lu(A)
    print("P: \n")
    for i in range(len(A)):
        for j in range(len(A)):
            print("%.3f " % P[i][j])
        print("\n")

    print("L: \n")
    for i in range(len(A)):
        for j in range(len(A)):
            print("%.3f " % L[i][j])
        print("\n")

    print("U: \n")
    for i in range(len(A)):
        for j in range(len(A)):
            print("%.3f " % U[i][j])
        print("\n")


main()
