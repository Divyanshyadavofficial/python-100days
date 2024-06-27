x = int(input("enter the value of x: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x) 



''' in match statments we do not have to put break statments
after every case and in these statments cases are checked if they 
satisfy the condition that case will be executed and others are left 
unevaluated and if any case does'nt matches the condition then the 
default case will be executed which is denoted by case _:'''