info = {'name':'Divyansh','age':21,'eligible':True}
print(info)
print(info['name'])
print(info.get('eligible'))
print(info.keys())
print(info.values())
print(info.items())


for key in info.keys():
    print(f"the value corresponding to the key is key {key} is {info[key]}")

for key,value in info.items():
    print(f"the value corresponding to the key {key} is {value}")