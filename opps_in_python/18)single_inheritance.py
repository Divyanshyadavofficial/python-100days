class Animal:
    def __init__(self, name,species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("sound made by animal")
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark")
class Cat(Animal):
    def __init__(self, name,breed):
        Animal.__init__(self,name,species = "cat")
        self.breed = breed
    def make_sound(self):
        print("meow")


d= Dog("Dog","shitzoo")
d.make_sound()
a= Animal("dog","dog")
a.make_sound()
c= Cat("cat","civet")
c.make_sound()