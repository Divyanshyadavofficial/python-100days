class employee:
    companyName = "apple"#class variable which is common to all instances of a class
    noofemployees = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        employee.noofemployees +=1
    def showDetails(self):
        print(f"the name of the employee is {self.name} and the raise amount in {self.noofemployees} sized {self.companyName} is {self.raise_amount}")
emp1= employee("divyansh")
emp1.raise_amount= 0.3
emp1.showDetails()
#the compile checks the instance variable if it is defined in the local 
#scope if not then it checks that the variable is present as class var
#takes the value of that class variable 
emp1.companyName = "apple india"#now company name is defined as the instance 
#variable which is used with the objects and methods which are defined
#for that instance.
emp1.showDetails()
#we can change the value of the class variable by using classname.varname= newname
#and this change will be refelected for all instances of that class.
employee.companyName = "google"
print(employee.companyName)
emp2 = employee("divya")
emp2.showDetails()        