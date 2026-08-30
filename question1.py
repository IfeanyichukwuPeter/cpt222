# Question 1(b)
# Substitution Method

# Equation 1:
# x + y + z = 6
#
# Therefore:
# x = 6 - y - z

# After substitution:
# 3y + z = 7
# y - 2z = -3

# From 3y + z = 7:
# z = 7 - 3y

# Substitute into y - 2z = -3:
# y - 2(7 - 3y) = -3
# 7y = 11
# y = 11/7

y = 11 / 7

# Find z
z = 7 - 3 * y

# Find x
x = 6 - y - z

print("Solution using Substitution Method:")
print("x =", x)
print("y =", y)
print("z =", z)

# Question 1(c)
# Jacobi Iteration Method

x = 0
y = 0

print("\nJacobi Iteration:")

for i in range(1, 6):

    # Calculate new values using OLD x and y
    new_x = (11 - y) / 10
    new_y = (12 - 2 * x) / 10

    x = new_x
    y = new_y

    print(f"Iteration {i}: x = {x:.6f}, y = {y:.6f}")
