class my_class:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"value is {self._value}")
    #getter
    @property
    def ten_value(self):
        return 10* self._value
    #setter
    @ten_value.setter
    def ten_value(self , new_value):
        self._value = new_value/10
   
obj = my_class(10)
obj.show()
obj.ten_value = 88
print(obj.ten_value)
