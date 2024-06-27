#with the help of class methods as alternative constructor we are 
#returning the instance of a class wuth the help of class method.

#cls(string.split("-")[0],int(string.split("-")[1]))

# is same as employee("divyansh",12000)

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
e1 = employee("divyansh",12000)
print(e1.name)
print(e1.salary)

string = "divya-12000"
e2 = employee.fromstr(string)
print(e2.name)
print(e2.salary)