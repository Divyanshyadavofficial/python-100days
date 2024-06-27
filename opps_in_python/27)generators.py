
def my_gen1():
    for i in range(5):
        yield i

gen = my_gen1()
print(next(gen))
print(next(gen))