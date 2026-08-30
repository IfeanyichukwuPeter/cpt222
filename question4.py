# Question 4(b)
# Newton-Raphson Method

def f(x):
    return x**2 - 5


def df(x):
    return 2 * x


# Initial guess
x = 2.0

# Number of iterations
iterations = 3

print("Newton-Raphson Method:")

for i in range(1, iterations + 1):

    x = x - f(x) / df(x)

    print(f"Iteration {i}: x = {x:.6f}")


print(f"\nApproximate root = {x:.6f}")

# Question 4(c)
# Euler's Method

def f(x, y):
    return 2 * x + y


# Initial conditions
x = 0.0
y = 1.0

# Step size
h = 0.1

# Number of steps
steps = 3

print("\nEuler's Method:")
print(f"Initial: x = {x:.1f}, y = {y:.6f}")

for i in range(1, steps + 1):

    # Euler formula
    y = y + h * f(x, y)

    # Move to the next x value
    x = x + h

    print(f"Step {i}: x = {x:.1f}, y = {y:.6f}")


print(f"\nApproximate y({x:.1f}) = {y:.6f}")