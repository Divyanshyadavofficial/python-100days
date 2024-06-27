def list():
    l = [1,2,3,4]
    num = int(input("enter the number "))
    try:
        print(l[num])
        return 1
    except:
        print("wrong input")
        return 0 
    finally:
        print("i am always executed")

f = list()
print(f)

# def list():
#     l = [1,2,3,4]
#     num = int(input("enter the number "))
#     try:
#         print(l[num])
#         return 1
#     except:
#         print("wrong input")
#         return 0 
# print("i am always executed")

# f = list()
# print(f)