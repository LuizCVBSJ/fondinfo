import math

def ellipse_area(a, b):
    return math.pi * a * b

def main():
    x = float(input("First Value?"))
    y = float(input("Second Value?"))
    print(str(ellipse_area(x, y)))

main()
