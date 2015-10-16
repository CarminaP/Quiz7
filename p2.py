def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        answer = fibonacci(n-1)+ fibonacci(n-2)
        return answer
x=int(input("Write a number: "))
print(("The ")+str(x)+("th number in the fibonacci series is: ")+str(fibonacci(x)))
