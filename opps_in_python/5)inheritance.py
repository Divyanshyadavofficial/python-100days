#single level inheritance
# class Employee:
#     def __init__(self, name,id):
#         self.name = name
#         self.id = id
#     def showDetails(self):
#         print(f"the name of the employee: {self.id} is {self.name}")
# class programmer(Employee):
#     def showAddress(self):
#         print("they belong to dronacharya")
# e1 = Employee("divyansh",1)
# e1.showDetails()
# e2 = programmer("digisha",2)
# e2.showDetails()
# e2.showAddress()

#multiple Inheritance
# class Mother:
#     mothername = "suman yadav"
#     def mother(self):
#         print(self.mothername)
# class Father:
#     fathername = "Satbir singh"
#     def father(self):
#         print(self.fathername)
# class Son(Mother, Father):
#     def parents(self):
#         print("Father name is: ",self.fathername)
#         print("Mother name is: ",self.mothername)
# s1 = Son()
# s1.parents()



#multilevel Inheritance
# class Grandfather:
#     def __init__(self,grandfathername):
#         self.grandfathername = grandfathername
# class Father(Grandfather):
#     def __init__(self,fathername, grandfathername):
#         self.fathername = fathername
#         Grandfather.__init__(self,grandfathername)
# class Son(Father):
#     def __init__(self,sonname ,fathername, grandfathername):
#         self.sonname = sonname
#         Father.__init__(self,fathername,grandfathername)
#     def print_name(self):
#         print('Grandfather name :',self.grandfathername)
#         print("Father name :",self.fathername)
#         print("Son name :", self.sonname)
# s1 = Son("divyansh","satbir","umrao")
# print(s1.grandfathername)
# s1.print_name()

#hierarichal inheritance

class parent:
    def func1(self):
        print("this function is in parent class")
class child1(parent):
    def func2(self):
        print("this function is in child 1")
class child2(parent):
    def func3(self):
        print("this function is in child 2")
obj1 = child1()
obj2 = child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()

#hybrid inheritance

class School:
    def func1(self):
        print("this function is in school")

class Student1(School):
    def func2(self):
        print("this function is in student 1")
class Student2(School):
    def func3(self):
        print("this function is in student 3")
class Student3(Student1,School):
    def func4(self):
        print("this function is in student 3")
object = Student3()
object.func1()
object.func2()