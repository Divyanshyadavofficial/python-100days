from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*2
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(4))
print("done for 4")


