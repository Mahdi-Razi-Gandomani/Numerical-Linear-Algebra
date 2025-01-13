import numpy as np
import time

# Initialize matrix size, a, b, c and f
n = 2000
a = np.zeros(n)
b = np.zeros(n)
c = np.zeros(n)
f = np.zeros(n)
for i in range(0, n):
    a[i] = 1
    b[i] = 3
    c[i] = 1
    f[i] = i + 1

# Start time of algorithm
t1 = time.time()

# Calculate alpha and beta
A = np.zeros(n)
B = np.zeros(n)
A[0] = b[0]
for i in range(1, n):
    B[i] = a[i] / A[i - 1]
    A[i] = b[i] - B[i]*c[i - 1]

# Calculate y
y = np.zeros(n)
y[0] = f[0]
for i in range(1, n):
    y[i] = f[i] - B[i]*y[i - 1]

# Calculate x
x = np.zeros(n)
x[n - 1] = y[n - 1] / A[n - 1]
for i in range(n - 2, -1, -1):
    x[i] = (y[i] - c[i] * x[i + 1]) / A[i]

# End time of algorithm
t2 = time.time()
print("took", t2 - t1, "seconds")

# Print out x
print(x)