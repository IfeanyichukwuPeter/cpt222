# Question 2(b)
# Elimination Method

# Augmented matrix
A = [
    [2.0, 1.0, -1.0, 8.0],
    [1.0, -1.0, 2.0, 3.0],
    [3.0, 2.0, 1.0, 13.0]
]

# Number of equations
n = 3

# Forward elimination
for i in range(n):

    for j in range(i + 1, n):

        factor = A[j][i] / A[i][i]

        for k in range(i, n + 1):
            A[j][k] = A[j][k] - factor * A[i][k]


# Back substitution
x = [0.0, 0.0, 0.0]

for i in range(n - 1, -1, -1):

    total = A[i][n]

    for j in range(i + 1, n):
        total = total - A[i][j] * x[j]

    x[i] = total / A[i][i]


# Display answer
print("Solution using Elimination Method:")
print(f"x = {x[0]:.4f}")
print(f"y = {x[1]:.4f}")
print(f"z = {x[2]:.4f}")

# Question 2(c)
# Bisection Method

def f(x):
    return x**3 - 4


# Initial interval
a = 1
b = 2

# Number of iterations
iterations = 5

print("\nBisection Method:")

for i in range(1, iterations + 1):

    # Find midpoint
    c = (a + b) / 2

    print(f"Iteration {i}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}")

    # Check which half contains the root
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print(f"\nApproximate root after {iterations} iterations = {c:.6f}")