def mcd(a, b):
    if b == 0:
        return a
    elif b > 0:
        return mcd(b, a % b)

a = int(input("\na?\n"))
b = int(input("\nb?\n"))

print(f"\nThe MCD of {a} and {b} is {mcd(a, b)}\n")
