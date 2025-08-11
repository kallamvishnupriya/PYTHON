a, b, c = sorted(map(float, input("Enter three sides: ").split()))

if a + b <= c:
    print("Not a triangle")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

if a**2 + b**2 == c**2:
    print("Right-angled")
