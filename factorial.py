def factorial (n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
num = int(input("Enter a Number: "))

if num < 0:
    print("sorry, factorial")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of",num,"is",factorial(num))