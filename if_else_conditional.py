#if conditional
a= int(input("Enter your age: "))
print("Your age is:",a)
#Conditional operators
# >,<,>=,<=,==,!=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if(a>18):
    print("You can drive")
    print("yes")
else:
    print("you cannot drive")
    print("No")



#elif conditional
num = int(input("Enter the value of num: "))
if (num<0):
    print("number is negative.")
elif(num ==0):
    print("Number is zero")
elif(num==999):
    print("Number is special")
else:
    print("number is positive")
print("I am happy now")


#nested_if_conditional
num = 18
if (num<0):
    print("number is negative")
elif(num>0):
    if(num<=10):
        print("number is between 1-10")
    elif(num>10 and num<=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("number is zero")


# go to school 
is_raining = bool(input("tell whether it is raining outside or not "))
if(is_raining==True):
    print("Today is a holiday ")
else:
    print("go to school bad luck today")