# Question 6(b)
# Newton Forward Interpolation

# Given data
x = [0, 1, 2]
y = [1, 3, 7]

# Calculate first differences
delta_y0 = y[1] - y[0]
delta_y1 = y[2] - y[1]

# Calculate second difference
delta2_y0 = delta_y1 - delta_y0

# Required value
value = 1.5

# Initial x value and interval
x0 = x[0]
h = x[1] - x[0]

# Calculate p
p = (value - x0) / h

# Newton Forward formula
result = (
    y[0]
    + p * delta_y0
    + (p * (p - 1) / 2) * delta2_y0
)

print("Newton Forward Interpolation:")
print(f"Delta y0 = {delta_y0}")
print(f"Delta y1 = {delta_y1}")
print(f"Delta^2 y0 = {delta2_y0}")
print(f"p = {p}")
print(f"\ny({value}) = {result:.4f}")

# Question 6(c)
# Lagrange Interpolation

# Given data points
x = [0, 1, 2]
y = [1, 3, 2]

# Value at which we want the polynomial
value = 1.5

# Number of data points
n = len(x)

result = 0.0

# Lagrange interpolation
for i in range(n):

    term = y[i]

    for j in range(n):

        if i != j:
            term = term * (value - x[j]) / (x[i] - x[j])

    result = result + term


print("Lagrange Interpolation:")
print(f"P({value}) = {result:.4f}")