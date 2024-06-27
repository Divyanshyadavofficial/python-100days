class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius*self.radius

obj1 = Circle(4)
print(obj1.area())
'''Method overriding is a powerful feature in object-oriented programming 
that allows you to redefine a method in a derived class.'''

'''When you create an instance of the derived class and call the overridden method,
 the version of the method in the derived class is executed,
   rather than the version in the base class.'''

class Shape1:
    def area1(self):
        print("Calculating area...")


class Circle1(Shape1):
    def __init__(self,radius1):
        self.radius1 = radius1
    def area1(self):
        print("Calculating area of a circle...")
        super().area1()
        return 3.14*self.radius1*self.radius1


obj2 = Circle1(3)
print(obj2.area1())

'''Another way to customize the behavior of a class is to call the base class method from the derived class method.
 To do this, you can use the super function. 
 The super function allows you to call the base class method from the derived class method, 
 and can be useful when you want to extend the behavior of the base class method, 
 rather than replace it.'''