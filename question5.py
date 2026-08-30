# Question 5(b)
# Gauss-Seidel Iteration Method

# Initial values
x = 0.0
y = 0.0
z = 0.0

# Number of iterations
iterations = 3

print("Gauss-Seidel Iteration:")

for i in range(1, iterations + 1):

    # Use the newest values immediately
    x = (12 - y - z) / 10
    y = (13 - 2 * x - z) / 10
    z = (14 - 2 * x - 2 * y) / 10

    print(f"Iteration {i}: x = {x:.6f}, y = {y:.6f}, z = {z:.6f}")

print("\nFinal approximation:")
print(f"x = {x:.6f}")
print(f"y = {y:.6f}")
print(f"z = {z:.6f}")

# Question 5(c)
# Runge-Kutta 4th Order Method

def f(x, y):
    return x + y


# Initial values
x = 0.0
y = 1.0

# Step size
h = 0.2

# Calculate k1
k1 = f(x, y)

# Calculate k2
k2 = f(x + h / 2, y + (h / 2) * k1)

# Calculate k3
k3 = f(x + h / 2, y + (h / 2) * k2)

# Calculate k4
k4 = f(x + h, y + h * k3)

# RK4 formula
y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

# Move to next x
x = x + h

print("\nRunge-Kutta 4th Order Method:")
print(f"k1 = {k1:.6f}")
print(f"k2 = {k2:.6f}")
print(f"k3 = {k3:.6f}")
print(f"k4 = {k4:.6f}")
print(f"y({x:.1f}) = {y:.6f}")