from quadratic import quadratic_solver

print("Case A")
print(quadratic_solver(0, 1, 2))

print("Case B")
print(quadratic_solver(1, 2, 1))

print("Case C")
print(quadratic_solver(1, 2, 2, complex_allowed=True))

print("Case D")
print(quadratic_solver(1, 5, 1, complex_allowed=True))