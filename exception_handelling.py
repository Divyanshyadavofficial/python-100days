a = (input("enter a num"))
try:
    for i in range(1,6):
        print(f"{int(a)}x {i} ={int(a)*i} ")
except:
    print("invalid Input")
print("other lines of code")

b = ["Divyansh","Sourabh","Tarun"]
try:
    c= int(input("enter a num"))
    print(b[c])
except:
    print("index error")

try:
    d = int(input("enter a integer"))
    print(d)
except:
    print("the entered number is not a integer")