import math

for a in [0, 45, 90, 135, 180]:
    v = math.sin(a * math.pi / 180)
    print(f"Angle: {a:3}; Sin: {v:4.5f}")
