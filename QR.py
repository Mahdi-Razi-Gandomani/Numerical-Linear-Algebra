import numpy as np

matrix = np.array([[3, 1, -2], [-2, 2, 2], [0, 1, 1]])
print("matrix:\n", matrix)
m, n = matrix.shape

a = []
for i in range(0, n):
    a.append(matrix[:, i])

q = [a[0]]
r = np.zeros((n, n))
r[0][0] = np.linalg.norm(q[0])

for i in range(1, n):
    s = 0
    for j in range(0, i):
        r[j][i] = np.dot(q[j], a[i]) / (np.linalg.norm(q[j]) ** 2)
        s += r[j][i] * q[j]
    q.append(a[i] - s)
    r[i][i] = np.linalg.norm(q[i])

R_hat = np.copy(r)
for i in range(0, n):
    R_hat[i][i] = 1

d = []
for i in range(0, n):
    d.append(r[i][i])
D = np.diag(d)
D_inv = np.linalg.inv(D)

R = np.dot(D, R_hat)
print("\nR:\n", R)

Q = np.dot(np.transpose(q), D_inv)
print("\nQ:\n", Q)