names = ("Divyansh","kunal","sourav","Tarun")
temp = list(names)
temp.append("Mridul")
names = tuple(temp)
print(names)
roll_no = (24226,24237,24257,24228)
name_roll = names+roll_no
print(name_roll)
tuple1=(0,1,2,3,4,5,5,1,2,4)
res = tuple1.count(3)
print(res)

res_index = tuple1.index(3,0,4)
print(res_index)