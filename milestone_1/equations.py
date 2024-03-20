import cmath

eq = '4x^2 +4x +    (-8) =  0'

eq = eq.replace(" ", "")
eq = eq.replace("(-", "-")
eq = eq.replace("+", "")

parts = eq.split("x^2")

a = int(parts[0])
parts = parts[1].split("x")
b = int(parts[0])
c = int(parts[1].replace("(", "").replace(")", "").replace("=", ""))

discriminant = cmath.sqrt(b**2 - 4*a*c)
x1 = (-b + discriminant) / (2*a)
x2 = (-b - discriminant) / (2*a)

print(f"Coefficients a, b, c: {a}, {b}, {c}")
print(f"Roots of the quadratic equation: {x1}, {x2}")