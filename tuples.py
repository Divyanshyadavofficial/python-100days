tuple1 = (1,2,3,4,5,6)
tuple2 = ("Red","Green","Blue")
print(tuple1)
print(tuple2)

print(tuple2[0])
print(tuple2[1])
print(tuple2[2])
print(tuple2[-1])
print(tuple2[-2])

if "Red" in tuple2:
    print("Red is present")
else:
    print("Red is absent")
print(tuple1[:])
print(tuple1[::2])
print(tuple1[0:7:3])