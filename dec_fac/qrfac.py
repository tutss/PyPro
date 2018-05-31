import numpy as np
import scipy.linalg


# Using Scipy lib for the QR factorization
def qr_scipy_example():
    A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])  # From the Wikipedia Article on QR Decomposition
    Q, R = scipy.linalg.qr(A)
    print('scipy q: \n', Q)
    print('scipy r: \n', R)


# My implementation
def transpose_matrix(M):
    return np.transpose(M)


def normalize_vector(u):
    return np.linalg.norm(u)


def multiply_matrix(M, N):
    m, n = M.shape
    m1, n1 = N.shape
    if (n != m1):
        return "Can't multiply"
    else:
        return np.matmul(M, N)
    return 0


def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = householder(A[i:, i])
        Q = np.dot(Q, H)
        A = np.dot(H, A)
    return Q, A


def householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    h = np.eye(a.shape[0])
    h -= (2 / np.dot(v[None, :], v[:, None])) * np.dot(v[:, None], v[None, :])
    return h


def main():
    A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
    Q, R = qr(A)
    print('q:\n', Q.round(6))
    print('r:\n', R.round(6))
    print('-----\n')
    qr_scipy_example()


main()
