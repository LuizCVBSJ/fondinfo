def fibonacci(n: int) -> int:
    result = 0
    if n <= 1:
        result = n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

number = int(input("Fibonacci of ?\n"))

print(fibonacci(number))
