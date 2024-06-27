import time
print(time.time())
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%D %H:%M:%S",t)
print(formatted_time)
print("Start:",time.time())
time.sleep(2)
print("End:",time.time())
init = time.time()
time.sleep(3)
t1 = time.time()-init
print(t1)