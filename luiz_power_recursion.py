def base_power(x, y):
    if x == 0 or y < 0:
        raise ValueError("Invalid x or y!")
    if y == 0:
        return 1
    return x * base_power(x, y-1)
base = int(input("Base?\n"))
power = int(input("\nPower?"))

print(base_power(base, power))

