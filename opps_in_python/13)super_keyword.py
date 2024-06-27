class parentClass:
    def parent_method(self):
        print("this is the parent method")
class childClass(parentClass):
    def child_method(self):
        print("this is the child method")
        super().parent_method()
child_obj = childClass()
child_obj.child_method()


class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang
divyansh = Employee("Divyansh yadav","1")
divya = programmer("Divya","2","Python")
print(divya.name)
print(divya.id)
print(divya.lang)
