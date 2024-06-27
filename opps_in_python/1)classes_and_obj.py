class person:
    name = "Divyansh"
    networth = 10
    occupation = "DataScience"
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a = person()
b = person()
c = person()
a.info()
a.name = "shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

a.info()
b.info()
c.info()