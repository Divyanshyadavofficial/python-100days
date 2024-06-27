# Default argument

def add(b,a=2):
    add = a+b
    print("the sum of a and b is ",add)
add(3)

def  name(fname,mname = "jhon",lname = "Whatson"):
    print("Hello,",fname , mname, lname)
name("Amy")
# keyword arguments
name(mname = "peter", lname = "Wesker", fname = "jade")
# required arguments
def  name(fname,lname,mname = "jhon"):
    print("Hello,",fname , mname, lname)
#name("peter") this will generate error cause lname is a required
    #argument which is not present in the function call

#when number of arguments passed matches the function defination.
name("peter","Ego","Quill") 
# arbitary variable length arguments

def add1(*numbers):
    for num in numbers:
        add = num+num+1
        print(add)
add1(1,2,3,4,5,6,7,8)


#keyword arbitrary arguments

def name(**name):#the function access the arguments by processing them in the form of dictionary. 
    print("Hello,",name["fname"], name["mname"],name["lname"])
name(mname = "Buchanan", lname = "Barnes",fname = "James")

#return statments

def add2(a,b):
    return(a+b)
c=print(add2(2,3))
