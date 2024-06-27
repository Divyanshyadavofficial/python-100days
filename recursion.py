#factorial of a number
def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return (num * factorial(num-1))
    
num = int(input("enter the number"))
print("Factorial: ",factorial(num))

#fibonacci series
def fibonacci(num):
    if(num==0 ):
        return 0
    elif(num==1):
        return 1 
    else:
        return(fibonacci(num-1)+fibonacci(num-2))
print("Fibonacci: ",fibonacci(num))