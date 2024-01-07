from functools import lru_cache

@lru_cache()  

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

number = int(input(("Choose the number for the Fibonacci sequence: ")))
print(fibonacci(number))
