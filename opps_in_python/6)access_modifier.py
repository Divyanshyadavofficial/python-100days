class Employee:
    def __init__(self):
        self.name = "divyansh"
        self.age = "21"
        self.__branch = "aiml"

a = Employee()
print(a.name) #this can be accesed from any where in the program
print(a.age) #this is the public and can be accessed directly
print(a._Employee__branch) #this is not public it is a private var
#which is defined by the convention __ and cannot be accessed directly
#and can be accessed indirectly by using a convention like a._classname__variable name.
#this concept of indirect access is called name mangling in python.
print(a.__dir__())

#protected acess modifier

class Student:
    def __init__(self):
        self._name = "divyansh"
    def _funName(self):
        return "divyu"
class Subject(Student):
    pass
obj = Student()
obj1 = Subject()

print(obj._name)
print(obj._funName())

print(obj1._name)
print(obj1._funName())