def greet(fx):
    def mfx(*args, **kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("hello")

@greet
def add(a,b):
    print(a+b)

hello()

add(1,2)