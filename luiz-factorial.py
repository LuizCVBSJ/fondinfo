def factorial(n: int) -> int:
    result = 1
    print(f"n is {n}")
    if n > 0:
        print(f"Starting factorial of {n-1}")
        print(f"Multiplying {n} by {n-1}")
        result = n * factorial(n-1)
    print(f"returning {result}")
    return result

number = int(input("Factorial of Number: \n"))

print(f"The factorial of the number {number} is {factorial(number)}")
