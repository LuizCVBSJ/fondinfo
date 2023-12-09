import math

class Ellipse:
    
    def __init__(self, a: float, b: float):
        self._a = a
        self._b = b

    def ellipse_area(self):
        return math.pi * self._a * self._b
    
    def focal_distance(self):
        return 2 * math.sqrt(abs((self._a ** 2) - (self._b ** 2)))

def main():
    x = float(input("First Value?"))
    y = float(input("Second Value?"))
    ellipse = Ellipse(x, y)
    print(str(ellipse.ellipse_area()))
    print(str(ellipse.focal_distance()))

main()
