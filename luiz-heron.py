print("Heron Function")
a = float(input("First side:"))
b = float(input("Second side:"))
c = float(input("Third side:"))

def heron(a: float, b: float, c: float) -> float:
    s = (a + b + c)/2
    return 0.5 ** (s * (s - a) * (s - b) * (s - c))
def main():
    print(str(heron(a, b, c)))
