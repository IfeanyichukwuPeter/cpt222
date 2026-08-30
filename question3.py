# Question 3(b)
# Fixed-Point Iteration Method

import math

# Initial value
x = 0.0

# Number of iterations
iterations = 6

print("Fixed-Point Iteration:")

for i in range(1, iterations + 1):

    # Fixed-point formula: x(n+1) = e^(-x(n))
    x = math.exp(-x)

    print(f"Iteration {i}: x = {x:.6f}")

print(f"\nApproximate value after {iterations} iterations = {x:.6f}")


# Question 3(c)
# LU Decomposition

# Matrix A
A = [
    [2.0, 3.0],
    [4.0, 1.0]
]

# Matrix B
B = [8.0, 10.0]

# Lower triangular matrix L
L = [
    [1.0, 0.0],
    [0.0, 1.0]
]

# Upper triangular matrix U
U = [
    [2.0, 3.0],
    [0.0, 0.0]
]

# Find L and U
factor = A[1][0] / A[0][0]

L[1][0] = factor

U[1][0] = 0
U[1][1] = A[1][1] - factor * A[0][1]

print("L matrix:")
for row in L:
    print(row)

print("\nU matrix:")
for row in U:
    print(row)


# Forward substitution: LY = B

y1 = B[0]

y2 = B[1] - L[1][0] * y1


# Back substitution: UX = Y

y = y2 / U[1][1]

x = (y1 - U[0][1] * y) / U[0][0]


print("\nSolution:")
print(f"x = {x:.4f}")
print(f"y = {y:.4f}")