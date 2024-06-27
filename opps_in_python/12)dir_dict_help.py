x=[1,2,3]
print(dir(x))

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version = 1
p = person("divyansh",21)
print(p.__dict__)

print(help(person))