def factorial(num):
    if(num==0 or num==1):
        return 1
    else:
        return(num*factorial(num-1))
num = int(input("Enter the value of num = 5"))
if(num<5 or num>5):
    raise ValueError("not a valid entry")
c=factorial(num)
print(f"the factorial of num is {c}")
try:
    a= input("enter any value between 5 and 9")
    if a.isdigit():
        a= int(a)
        if 5<=a<=9:
            print("the input value is ",a)
        elif a=="quit":
            pass
        else:
            raise ValueError("please enter an appropriate value")
except ValueError as e:
    print(e)


    


