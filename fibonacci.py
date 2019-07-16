def fibonacci (n):
    if n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
num = int(input("Enter a Number: "))

if num ==1:
    print("sorry, enter a positive number")
else:
#    for a in range(num):
#        print("The fibonacci of",num,"is",fibonacci(num))
#         print(fibonacci(a))
     print(list(map(fibonacci,range(1,num))))