a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + (delta)**0.5) / (2 * a)
    x2 = (-b - (delta)**0.5) / (2 * a)
    print("Real:", {x1} , {x2})
elif delta == 0:
    x = -b / (2 * a)
    print("Duplicate:",{x})
else:
    x1 = (-b + (delta)**0.5) / (2 * a)
    x2 = (-b - (delta)**0.5) / (2 * a)
    print("Complex:", {x1} , {x2})
