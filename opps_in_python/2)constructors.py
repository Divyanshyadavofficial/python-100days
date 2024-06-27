class person:
    def __init__(self,name,occ):
        print("Hey I am a person")
        self.name = name
        self.occ = occ
    def info(self):
        print(f"{self.name} is a {self.occ}")
a = person("divyansh","datascientist")
b = person("digisha","Hr")
a.info()
b.info()