class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
class person(Human):
    def __init__(self,name,age,address):
        Human.__init__(self,name,age)
        self.address = address
    def show_details(self):
        Human.show_details(self)
        print("Address :", self.address)
class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration
    def show_details(self):
        print("program name:", self.program_name)
        print("Duration:",self.duration)
class Student(person):
    def __init__(self, name, age, address, program):
        person.__init__(self, name, age, address)
        self.program = program
    def show_details(self):
        person.show_details(self)
        self.program.show_details()
Program = Program("computer science",4)
student = Student("Divyansh",21,"123 Main st.",Program)
student.show_details()
