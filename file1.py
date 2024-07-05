def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

result = factorial(5)
print(f"Factorial of 5 is: {result}")
