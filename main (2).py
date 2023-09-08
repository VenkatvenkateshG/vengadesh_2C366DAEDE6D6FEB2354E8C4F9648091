def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Input a value for which you want to calculate the factorial
number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")

