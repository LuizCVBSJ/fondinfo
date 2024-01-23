def f(x: float) -> float:
    return x**3 - x - 1

def find_zero(a: float, b: float):
    half = (a + b) / 2
    f_half = f(half)
    
    if f(a) * f(b) > 0:
        raise ValueError("f Doesn't cross the x-axis")
    if abs(f_half) < 0.001:
        return half
    elif f_half * f(a) < 0:
        return find_zero(a, half)  
    else:
        return find_zero(half, b)

def main():
    print(find_zero(1, 2))

main()
